from django import forms
from django.utils.safestring import mark_safe

from core.environment import env
from sample.models import Store


class CoordinateWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(f"""
        <div id="naver-map" style="width:500px; height:500px;">
        <script>
            const fieldLatitude = document.getElementsByClassName("field-latitude")[0];
            fieldLatitude.style.display = "none";

            const fieldLongitude = document.getElementsByClassName("field-longitude")[0];
            fieldLongitude.style.display = "none";

            const latitudeInput = document.getElementsByName("latitude")[0];
            const longitudeInput = document.getElementsByName("longitude")[0];
            const addressInput = document.getElementsByName("address")[0];

            const map = new naver.maps.Map('naver-map', {{
                center: new naver.maps.LatLng(37.3595704, 127.105399),
                zoom: 16
            }});
            const marker = new naver.maps.Marker({{
                position: new naver.maps.LatLng(37.3595704, 127.105399),
                map: map
            }});

            const searchCoordinateToAddress = (latlng)=>{{
                naver.maps.Service.reverseGeocode({{
                    coords: latlng,
                    orders: [
                        naver.maps.Service.OrderType.ADDR,
                        naver.maps.Service.OrderType.ROAD_ADDR
                    ].join(',')
                }}, (status, response)=>{{
                    if (status === naver.maps.Service.Status.ERROR) {{
                        return alert('Something Wrong!');
                    }}
                    addressInput.value = response.v2.address.jibunAddress;

                    latitudeInput.value = latlng.y;
                    longitudeInput.value = latlng.x;
                }});
            }};
            const searchAddressToCoordinate = (address)=>{{
                naver.maps.Service.geocode({{
                    query: address
                }}, (status, response)=>{{
                    if (status === naver.maps.Service.Status.ERROR) {{
                        return alert('Something Wrong!');
                    }}

                    if (response.v2.meta.totalCount === 0) {{
                        return alert("검색 결과가 없습니다. 주소를 정확히 입력해주세요.");
                    }}
                    const result = response.v2.addresses[0];
                    addressInput.value = result.jibunAddress;
                    point = new naver.maps.Point(result.x, result.y);

                    map.setCenter(point);
                    marker.setPosition(point);

                    latitudeInput.value = result.y;
                    longitudeInput.value = result.x;
                }});
            }};

            naver.maps.Event.addListener(map, 'click', (e)=>{{
                marker.setPosition(e.coord);
                searchCoordinateToAddress(e.coord);
            }});
            addressInput.addEventListener("keydown", (e)=>{{
                if (e.key === "Enter") {{
                    e.preventDefault();
                    searchAddressToCoordinate(addressInput.value);
                }}
            }});
            // addressInput.addEventListener("blur", ()=>{{
            //     searchAddressToCoordinate(addressInput.value);
            // }});
        </script>
        """)

    
class BitmaskDayWidget(forms.CheckboxSelectMultiple):
    DAY_CHOICES = [
        (1, "일"),
        (2, "월"),
        (4, "화"),
        (8, "수"),
        (16, "목"),
        (32, "금"),
        (64, "토"),
    ]

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=self.DAY_CHOICES)


class StoreAdminForm(forms.ModelForm):
    coordinate = forms.Field(widget=CoordinateWidget(), required=False)
    business_day = forms.MultipleChoiceField(
        choices=BitmaskDayWidget.DAY_CHOICES,
        widget=BitmaskDayWidget()
    )

    class Media:
        js = (
            f"https://oapi.map.naver.com/openapi/v3/maps.js?ncpKeyId={env.get('NCP_KEY_ID')}&submodules=geocoder",
        )

    class Meta:
        model = Store
        fields = (
            "store_categories",
            "title",
            "address",
            "latitude",
            "longitude",
            "coordinate",
            "description",
            "business_day",
            "start_date",
            "end_date",
            "opening_time",
            "closing_time",
            "profile_img_stored_files_group",
            "pre_order_start_at",
            "status"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and isinstance(self.instance.business_day, int):
            # int → list[str]
            self.initial['business_day'] = [
                str(day) for day, _ in BitmaskDayWidget.DAY_CHOICES
                if self.instance.business_day & day
            ]

    def clean_business_day(self):
        # list[str] → int
        values = self.cleaned_data.get("business_day", [])
        return sum(int(value) for value in values)
