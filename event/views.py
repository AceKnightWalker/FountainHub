from django.shortcuts import render
from django.views import generic
from .models import Event
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView


class IndexView(generic.ListView):
    paginate_by = 6
    context_object_name = 'event_list'

    def get_queryset(self):

        return Event.objects.order_by('-start_date')


class DetailView(generic.DetailView):
    model = Event


class EventYearArchiveView(YearArchiveView):
    queryset = Event.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True


class EventMonthArchiveView(MonthArchiveView):
    queryset = Event.objects.all()
    date_field = "date"
    allow_future = True
