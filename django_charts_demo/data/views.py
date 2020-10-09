import pandas as pd
import numpy as np
from django.views.generic import TemplateView
from .methods import csv_to_db
from .models import Purchase
from .charts import objects_to_df, Chart

PALETTE = ['#465b65', '#184c9c', '#d33035', '#ffc107', '#28a745', '#6f7f8c', '#6610f2', '#6e9fa5', '#fd7e14', '#e83e8c', '#17a2b8', '#6f42c1' ]

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):

        # get the data from the default method
        context = super().get_context_data(**kwargs)

        # the fields we will use
        # df_fields = ['city', 'customer_type', 'gender', 'unit_price', 'quantity', 
        #     'product_line', 'tax', 'total' , 'date', 'time', 'payment', 
        #     'cogs', 'profit', 'rating']

        # fields to exclude
        # df_exclude = ['id', 'cogs']
        
        # create a datframe with all the records.  chart.js doesn't deal well 
        # with dates in all situations so our method will convert them to strings
        # however we will need to identify the date columns and the format we want.
        # I am useing just month and year here.
        df = objects_to_df(Purchase, date_cols=['%Y-%m', 'date'])

        # create a charts context to hold all of the charts
        context['charts'] = []

        ### every chart is added the same way so I will just document the first one
        # create a chart object with a unique chart_id and color palette
        # if not chart_id or color palette is provided these will be randomly generated 
        # the type of charts does need to be identified here and might iffer from the chartjs type
        city_payment_radar = Chart('radar', chart_id='city_payment_radar', palette=PALETTE)
        # create a pandas pivot_table based on the fields and aggregation we want
        # stacks are used for either grouping or stacking a certain column
        city_payment_radar.from_df(df, values='total', stacks=['payment'], labels=['city'])
        # add the presentation of the chart to the charts context
        context['charts'].append(city_payment_radar.get_presentation())

        exp_polar = Chart('polarArea', chart_id='polar01', palette=PALETTE)
        exp_polar.from_df(df, values='total', labels=['payment'])
        context['charts'].append(exp_polar.get_presentation())

        exp_doughnut = Chart('doughnut', chart_id='doughnut01', palette=PALETTE)
        exp_doughnut.from_df(df, values='total', labels=['city'])
        context['charts'].append(exp_doughnut.get_presentation())

        exp_bar = Chart('bar', chart_id='bar01', palette=PALETTE)
        exp_bar.from_df(df, values='total', labels=['city'])
        context['charts'].append(exp_bar.get_presentation())

        city_payment = Chart('groupedBar', chart_id='city_payment', palette=PALETTE)
        city_payment.from_df(df, values='total', stacks=['payment'], labels=['date'])
        context['charts'].append(city_payment.get_presentation())

        city_payment_h = Chart('horizontalBar', chart_id='city_payment_h', palette=PALETTE)
        city_payment_h.from_df(df, values='total', stacks=['payment'], labels=['city'])
        context['charts'].append(city_payment_h.get_presentation())

        city_gender_h = Chart('stackedHorizontalBar', chart_id='city_gender_h', palette=PALETTE)
        city_gender_h.from_df(df, values='total', stacks=['gender'], labels=['city'])
        context['charts'].append(city_gender_h.get_presentation())

        city_gender = Chart('stackedBar', chart_id='city_gender', palette=PALETTE)
        city_gender.from_df(df, values='total', stacks=['gender'], labels=['city'])
        context['charts'].append(city_gender.get_presentation())

        return context

          
        



    

        
