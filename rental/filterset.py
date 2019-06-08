class BorrowedFilterSet(django_filters.FilterSet):
   missing = django_filters.BooleanFilter(field_name='returned', lookup_expr='isnull')

   class Meta:
       model = models.Borrowed
       fields = ['what', 'to_who', 'missing']
