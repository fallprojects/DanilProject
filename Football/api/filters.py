from django_filters import FilterSet,OrderingFilter
from .models import *

class TableFilterSet(FilterSet):
    o = OrderingFilter(
        fields=(
            ('matches', 'matches')
        )
    )
    o1 = OrderingFilter(
        fields=(
            ('goals_scored', 'goals_scored')
        ),
    field_labels={
        'goals_scored': 'GS',
        }
    )
    o2 = OrderingFilter(
        fields=(
            ('goals_conceded', 'goals_conceded')
        ),
    field_labels={
        'goals_conceded': 'GC',
       }
    )
    o3 = OrderingFilter(
        fields=(
            ('points', 'points')
        )
    )


    class Meta:
        model = Teams
        fields = '__all__'
        exclude = ['name','position','matches','points','goals_scored','goals_conceded']



