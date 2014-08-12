import datetime
from haystack import indexes
from library.models import Paper, Keyword, Author

class PaperIndex(indexes.SearchIndex, indexes.Indexable):
	title = indexes.CharField(document=True, use_template=True)
	authors = indexes.CharField(model_attr='authors')
	pub_date = indexes.DateTimeField(model_attr='pub_date')

	def get_model(self):
		return Paper

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
