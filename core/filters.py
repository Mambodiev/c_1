import django_filters
from django_filters import  CharFilter

from cart.models import Product

class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	title = CharFilter(field_name='title', lookup_expr='icontains')


	class Meta:
		model = Product
		fields = '__all__'
		exclude = ['date_created', 'featured',
		'title_en',
		'slug',
		'price',
		'updated',
		'created',
		'active',
		'available_sizes',
		'ForeignKey',
		'secondary_categories',
		'stock'
		'title_en',
		'title_fr',
		'slug_en',
		'slug_fr',
		'available_colours',
		'available_colours_en',
		'available_colours_fr',
		'available_sizes_en',
		'available_sizes_fr',
		'primary_category_en',
		'primary_category_fr',
		'primary_category',
		'stock']