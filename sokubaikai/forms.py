from django import forms

from .models import DoujinMarketsM


class DoujinMarketsMForm(forms.ModelForm):
    class Meta:
        model = DoujinMarketsM
        fields = ("id",
                  "market_name",
                  "market_version",
                  "market_place",
                  "market_date",
                  "market_start_time",
                  "market_memo")
