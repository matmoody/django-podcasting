from django.views.generic import DetailView, ListView

from podcasting.models import Episode, Show


class ShowListView(ListView):
    def get_queryset(self):
        return Show.objects.onsite()


class ShowDetailView(DetailView):
    def get_queryset(self):
        return Show.objects.onsite()


class EpisodeListView(ListView):
    def get_queryset(self):
        return Episode.objects.published().filter(show__slug=self.kwargs["show_slug"])


class EpisodeDetailView(DetailView):
    def get_queryset(self):
        return Episode.objects.published().filter(show__slug=self.kwargs["show_slug"])
