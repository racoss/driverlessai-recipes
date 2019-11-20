"""Flag for whether a date falls on a public holiday in Mexico DAI- rel: 1.8.0"""
from h2oaicore.transformer_utils import CustomTransformer
import datatable as dt
import numpy as np
import pandas as pd


# https://github.com/racoss/mexico_public_holidays

def make_holiday_frame():
   return dt.fread(


"""
Date,Name,Day,Observance,Observance Strategy,Type
1/1/2016,New Year's Day,Friday,1/1/2016,acutal_day,National holiday
1/6/2016,Day of the Holy Kings,Wednesday,1/6/2016,acutal_day,Observance
2/1/2016,Day off for Constitution Day,Monday,2/1/2016,acutal_day,National holiday
2/2/2016,Candlemas,Tuesday,2/2/2016,acutal_day,Observance
2/5/2016,Constitution Day,Friday,2/5/2016,acutal_day,National holiday
2/10/2016,Ash Wednesday,Wednesday,2/10/2016,acutal_day,"Observance, Christian"
2/14/2016,Valentine's Day,Sunday,2/14/2016,acutal_day,Observance
2/24/2016,Flag Day,Wednesday,2/24/2016,acutal_day,Observance
3/18/2016,Oil Expropriation Day,Friday,3/18/2016,acutal_day,Observance
3/19/2016,March Equinox,Saturday,3/19/2016,acutal_day,Season
3/20/2016,Palm Sunday,Sunday,3/20/2016,acutal_day,"Observance, Christian"
3/21/2016,Benito Juárez's Birthday Memorial,Monday,3/21/2016,acutal_day,National holiday
3/24/2016,Maundy Thursday,Thursday,3/24/2016,acutal_day,Bank holiday
3/25/2016,Good Friday,Friday,3/25/2016,acutal_day,Bank holiday
3/26/2016,Holy Saturday,Saturday,3/26/2016,acutal_day,Observance
3/27/2016,Easter Sunday,Sunday,3/27/2016,acutal_day,"Observance, Christian"
4/30/2016,Children's Day,Saturday,4/30/2016,acutal_day,Observance
5/1/2016,Labor Day / May Day,Sunday,5/1/2016,acutal_day,National holiday
5/5/2016,Battle of Puebla (Cinco de Mayo),Thursday,5/5/2016,acutal_day,Common local holiday
5/5/2016,Ascension Day,Thursday,5/5/2016,acutal_day,Observance
5/10/2016,Mother's Day,Tuesday,5/10/2016,acutal_day,Observance
5/15/2016,Teacher's Day,Sunday,5/15/2016,acutal_day,Observance
5/15/2016,Whit Sunday,Sunday,5/15/2016,acutal_day,Observance
5/26/2016,Corpus Christi,Thursday,5/26/2016,acutal_day,Observance
6/19/2016,Father's Day,Sunday,6/19/2016,acutal_day,Observance
6/20/2016,June Solstice,Monday,6/20/2016,acutal_day,Season
8/15/2016,Assumption of Mary,Monday,8/15/2016,acutal_day,Observance
9/15/2016,Shout of Dolores,Thursday,9/15/2016,acutal_day,Observance
9/16/2016,Independence Day,Friday,9/16/2016,acutal_day,National holiday
9/22/2016,September Equinox,Thursday,9/22/2016,acutal_day,Season
10/12/2016,Columbus Day,Wednesday,10/12/2016,acutal_day,Observance
10/31/2016,Halloween,Monday,10/31/2016,acutal_day,Observance
11/1/2016,All Saints' Day,Tuesday,11/1/2016,acutal_day,Observance
11/2/2016,All Souls' Day,Wednesday,11/2/2016,acutal_day,Observance
11/20/2016,Revolution Day Memorial,Sunday,11/20/2016,acutal_day,National holiday
11/20/2016,Christ the King Day,Sunday,11/20/2016,acutal_day,Observance
11/21/2016,Day off for Revolution Day Memorial,Monday,11/21/2016,acutal_day,National holiday
12/8/2016,Feast of the Immaculate Conception,Thursday,12/8/2016,acutal_day,Observance
12/12/2016,Day of the Virgin of Guadalupe,Monday,12/12/2016,acutal_day,Bank holiday
12/21/2016,December Solstice,Wednesday,12/21/2016,acutal_day,Season
12/24/2016,Christmas Eve,Saturday,12/24/2016,acutal_day,"Observance, Christian"
12/25/2016,Christmas Day,Sunday,12/25/2016,acutal_day,"National holiday, Christian"
12/28/2016,Day of the Holy Innocents,Wednesday,12/28/2016,acutal_day,Observance
12/31/2016,New Year's Eve,Saturday,12/31/2016,acutal_day,Observance
1/1/2017,New Year's Day,Sunday,1/1/2017,acutal_day,National holiday
1/6/2017,Day of the Holy Kings,Friday,1/6/2017,acutal_day,Observance
2/2/2017,Candlemas,Thursday,2/2/2017,acutal_day,Observance
2/5/2017,Constitution Day,Sunday,2/5/2017,acutal_day,National holiday
2/6/2017,Day off for Constitution Day,Monday,2/6/2017,acutal_day,National holiday
2/14/2017,Valentine's Day,Tuesday,2/14/2017,acutal_day,Observance
2/24/2017,Flag Day,Friday,2/24/2017,acutal_day,Observance
3/1/2017,Ash Wednesday,Wednesday,3/1/2017,acutal_day,"Observance, Christian"
3/18/2017,Oil Expropriation Day,Saturday,3/18/2017,acutal_day,Observance
3/20/2017,March Equinox,Monday,3/20/2017,acutal_day,Season
3/20/2017,Day off for Benito Juárez's Birthday Memorial,Monday,3/20/2017,acutal_day,National holiday
3/21/2017,Benito Juárez's Birthday Memorial,Tuesday,3/21/2017,acutal_day,National holiday
4/9/2017,Palm Sunday,Sunday,4/9/2017,acutal_day,"Observance, Christian"
4/13/2017,Maundy Thursday,Thursday,4/13/2017,acutal_day,Bank holiday
4/14/2017,Good Friday,Friday,4/14/2017,acutal_day,Bank holiday
4/15/2017,Holy Saturday,Saturday,4/15/2017,acutal_day,Observance
4/16/2017,Easter Sunday,Sunday,4/16/2017,acutal_day,"Observance, Christian"
4/30/2017,Children's Day,Sunday,4/30/2017,acutal_day,Observance
5/1/2017,Labor Day / May Day,Monday,5/1/2017,acutal_day,National holiday
5/5/2017,Battle of Puebla (Cinco de Mayo),Friday,5/5/2017,acutal_day,Common local holiday
5/10/2017,Mother's Day,Wednesday,5/10/2017,acutal_day,Observance
5/15/2017,Teacher's Day,Monday,5/15/2017,acutal_day,Observance
5/25/2017,Ascension Day,Thursday,5/25/2017,acutal_day,Observance
6/4/2017,Whit Sunday,Sunday,6/4/2017,acutal_day,Observance
6/15/2017,Corpus Christi,Thursday,6/15/2017,acutal_day,Observance
6/18/2017,Father's Day,Sunday,6/18/2017,acutal_day,Observance
6/20/2017,June Solstice,Tuesday,6/20/2017,acutal_day,Season
8/15/2017,Assumption of Mary,Tuesday,8/15/2017,acutal_day,Observance
9/15/2017,Shout of Dolores,Friday,9/15/2017,acutal_day,Observance
9/16/2017,Independence Day,Saturday,9/16/2017,acutal_day,National holiday
9/22/2017,September Equinox,Friday,9/22/2017,acutal_day,Season
10/12/2017,Columbus Day,Thursday,10/12/2017,acutal_day,Observance
10/31/2017,Halloween,Tuesday,10/31/2017,acutal_day,Observance
11/1/2017,All Saints' Day,Wednesday,11/1/2017,acutal_day,Observance
11/2/2017,All Souls' Day,Thursday,11/2/2017,acutal_day,Observance
11/20/2017,Revolution Day Memorial,Monday,11/20/2017,acutal_day,National holiday
11/26/2017,Christ the King Day,Sunday,11/26/2017,acutal_day,Observance
12/8/2017,Feast of the Immaculate Conception,Friday,12/8/2017,acutal_day,Observance
12/12/2017,Day of the Virgin of Guadalupe,Tuesday,12/12/2017,acutal_day,Bank holiday
12/21/2017,December Solstice,Thursday,12/21/2017,acutal_day,Season
12/24/2017,Christmas Eve,Sunday,12/24/2017,acutal_day,"Observance, Christian"
12/25/2017,Christmas Day,Monday,12/25/2017,acutal_day,"National holiday, Christian"
12/28/2017,Day of the Holy Innocents,Thursday,12/28/2017,acutal_day,Observance
12/31/2017,New Year's Eve,Sunday,12/31/2017,acutal_day,Observance
1/1/2018,New Year's Day,Monday,1/1/2018,acutal_day,National holiday
1/6/2018,Day of the Holy Kings,Saturday,1/6/2018,acutal_day,Observance
2/2/2018,Candlemas,Friday,2/2/2018,acutal_day,Observance
2/5/2018,Constitution Day,Monday,2/5/2018,acutal_day,National holiday
2/14/2018,Valentine's Day,Wednesday,2/14/2018,acutal_day,Observance
2/14/2018,Ash Wednesday,Wednesday,2/14/2018,acutal_day,"Observance, Christian"
2/24/2018,Flag Day,Saturday,2/24/2018,acutal_day,Observance
3/18/2018,Oil Expropriation Day,Sunday,3/18/2018,acutal_day,Observance
3/19/2018,Day off for Benito Juárez's Birthday Memorial,Monday,3/19/2018,acutal_day,National holiday
3/20/2018,March Equinox,Tuesday,3/20/2018,acutal_day,Season
3/21/2018,Benito Juárez's Birthday Memorial,Wednesday,3/21/2018,acutal_day,National holiday
3/25/2018,Palm Sunday,Sunday,3/25/2018,acutal_day,"Observance, Christian"
3/29/2018,Maundy Thursday,Thursday,3/29/2018,acutal_day,Bank holiday
3/30/2018,Good Friday,Friday,3/30/2018,acutal_day,Bank holiday
3/31/2018,Holy Saturday,Saturday,3/31/2018,acutal_day,Observance
4/1/2018,Easter Sunday,Sunday,4/1/2018,acutal_day,"Observance, Christian"
4/30/2018,Children's Day,Monday,4/30/2018,acutal_day,Observance
5/1/2018,Labor Day / May Day,Tuesday,5/1/2018,acutal_day,National holiday
5/5/2018,Battle of Puebla (Cinco de Mayo),Saturday,5/5/2018,acutal_day,Common local holiday
5/10/2018,Mother's Day,Thursday,5/10/2018,acutal_day,Observance
5/10/2018,Ascension Day,Thursday,5/10/2018,acutal_day,Observance
5/15/2018,Teacher's Day,Tuesday,5/15/2018,acutal_day,Observance
5/20/2018,Whit Sunday,Sunday,5/20/2018,acutal_day,Observance
5/31/2018,Corpus Christi,Thursday,5/31/2018,acutal_day,Observance
6/17/2018,Father's Day,Sunday,6/17/2018,acutal_day,Observance
6/21/2018,June Solstice,Thursday,6/21/2018,acutal_day,Season
7/1/2018,Mexican general election,Sunday,7/1/2018,acutal_day,National holiday
8/15/2018,Assumption of Mary,Wednesday,8/15/2018,acutal_day,Observance
9/15/2018,Shout of Dolores,Saturday,9/15/2018,acutal_day,Observance
9/16/2018,Independence Day,Sunday,9/16/2018,acutal_day,National holiday
9/22/2018,September Equinox,Saturday,9/22/2018,acutal_day,Season
10/12/2018,Columbus Day,Friday,10/12/2018,acutal_day,Observance
10/31/2018,Halloween,Wednesday,10/31/2018,acutal_day,Observance
11/1/2018,All Saints' Day,Thursday,11/1/2018,acutal_day,Observance
11/2/2018,All Souls' Day,Friday,11/2/2018,acutal_day,Observance
11/19/2018,Day off for Revolution Day Memorial,Monday,11/19/2018,acutal_day,National holiday
11/20/2018,Revolution Day Memorial,Tuesday,11/20/2018,acutal_day,National holiday
11/25/2018,Christ the King Day,Sunday,11/25/2018,acutal_day,Observance
12/1/2018,Inauguration day,Saturday,12/1/2018,acutal_day,National holiday
12/8/2018,Feast of the Immaculate Conception,Saturday,12/8/2018,acutal_day,Observance
12/12/2018,Day of the Virgin of Guadalupe,Wednesday,12/12/2018,acutal_day,Bank holiday
12/21/2018,December Solstice,Friday,12/21/2018,acutal_day,Season
12/24/2018,Christmas Eve,Monday,12/24/2018,acutal_day,"Observance, Christian"
12/25/2018,Christmas Day,Tuesday,12/25/2018,acutal_day,"National holiday, Christian"
12/28/2018,Day of the Holy Innocents,Friday,12/28/2018,acutal_day,Observance
12/31/2018,New Year's Eve,Monday,12/31/2018,acutal_day,Observance
1/1/2019,New Year's Day,Tuesday,1/1/2019,acutal_day,National holiday
1/6/2019,Day of the Holy Kings,Sunday,1/6/2019,acutal_day,Observance
2/2/2019,Candlemas,Saturday,2/2/2019,acutal_day,Observance
2/4/2019,Day off for Constitution Day,Monday,2/4/2019,acutal_day,National holiday
2/5/2019,Constitution Day,Tuesday,2/5/2019,acutal_day,National holiday
2/14/2019,Valentine's Day,Thursday,2/14/2019,acutal_day,Observance
2/24/2019,Flag Day,Sunday,2/24/2019,acutal_day,Observance
3/6/2019,Ash Wednesday,Wednesday,3/6/2019,acutal_day,"Observance, Christian"
3/18/2019,Oil Expropriation Day,Monday,3/18/2019,acutal_day,Observance
3/18/2019,Day off for Benito Juárez's Birthday Memorial,Monday,3/18/2019,acutal_day,National holiday
3/20/2019,March Equinox,Wednesday,3/20/2019,acutal_day,Season
3/21/2019,Benito Juárez's Birthday Memorial,Thursday,3/21/2019,acutal_day,National holiday
4/14/2019,Palm Sunday,Sunday,4/14/2019,acutal_day,"Observance, Christian"
4/18/2019,Maundy Thursday,Thursday,4/18/2019,acutal_day,Bank holiday
4/19/2019,Good Friday,Friday,4/19/2019,acutal_day,Bank holiday
4/20/2019,Holy Saturday,Saturday,4/20/2019,acutal_day,Observance
4/21/2019,Easter Sunday,Sunday,4/21/2019,acutal_day,"Observance, Christian"
4/30/2019,Children's Day,Tuesday,4/30/2019,acutal_day,Observance
5/1/2019,Labor Day / May Day,Wednesday,5/1/2019,acutal_day,National holiday
5/5/2019,Battle of Puebla (Cinco de Mayo),Sunday,5/5/2019,acutal_day,Common local holiday
5/10/2019,Mother's Day,Friday,5/10/2019,acutal_day,Observance
5/15/2019,Teacher's Day,Wednesday,5/15/2019,acutal_day,Observance
5/30/2019,Ascension Day,Thursday,5/30/2019,acutal_day,Observance
6/9/2019,Whit Sunday,Sunday,6/9/2019,acutal_day,Observance
6/16/2019,Father's Day,Sunday,6/16/2019,acutal_day,Observance
6/20/2019,Corpus Christi,Thursday,6/20/2019,acutal_day,Observance
6/21/2019,June Solstice,Friday,6/21/2019,acutal_day,Season
8/15/2019,Assumption of Mary,Thursday,8/15/2019,acutal_day,Observance
9/15/2019,Shout of Dolores,Sunday,9/15/2019,acutal_day,Observance
9/16/2019,Independence Day,Monday,9/16/2019,acutal_day,National holiday
9/23/2019,September Equinox,Monday,9/23/2019,acutal_day,Season
10/12/2019,Columbus Day,Saturday,10/12/2019,acutal_day,Observance
10/31/2019,Halloween,Thursday,10/31/2019,acutal_day,Observance
11/1/2019,All Saints' Day,Friday,11/1/2019,acutal_day,Observance
11/2/2019,All Souls' Day,Saturday,11/2/2019,acutal_day,Observance
11/18/2019,Day off for Revolution Day Memorial,Monday,11/18/2019,acutal_day,National holiday
11/20/2019,Revolution Day Memorial,Wednesday,11/20/2019,acutal_day,National holiday
11/24/2019,Christ the King Day,Sunday,11/24/2019,acutal_day,Observance
12/8/2019,Feast of the Immaculate Conception,Sunday,12/8/2019,acutal_day,Observance
12/12/2019,Day of the Virgin of Guadalupe,Thursday,12/12/2019,acutal_day,Bank holiday
12/21/2019,December Solstice,Saturday,12/21/2019,acutal_day,Season
12/24/2019,Christmas Eve,Tuesday,12/24/2019,acutal_day,"Observance, Christian"
12/25/2019,Christmas Day,Wednesday,12/25/2019,acutal_day,"National holiday, Christian"
12/28/2019,Day of the Holy Innocents,Saturday,12/28/2019,acutal_day,Observance
12/31/2019,New Year's Eve,Tuesday,12/31/2019,acutal_day,Observance
1/1/2020,New Year's Day,Wednesday,1/1/2020,acutal_day,National holiday
1/6/2020,Day of the Holy Kings,Monday,1/6/2020,acutal_day,Observance
2/2/2020,Candlemas,Sunday,2/2/2020,acutal_day,Observance
2/3/2020,Day off for Constitution Day,Monday,2/3/2020,acutal_day,National holiday
2/5/2020,Constitution Day,Wednesday,2/5/2020,acutal_day,National holiday
2/14/2020,Valentine's Day,Friday,2/14/2020,acutal_day,Observance
2/24/2020,Flag Day,Monday,2/24/2020,acutal_day,Observance
2/26/2020,Ash Wednesday,Wednesday,2/26/2020,acutal_day,"Observance, Christian"
3/16/2020,Day off for Benito Juárez's Birthday Memorial,Monday,3/16/2020,acutal_day,National holiday
3/18/2020,Oil Expropriation Day,Wednesday,3/18/2020,acutal_day,Observance
3/19/2020,March Equinox,Thursday,3/19/2020,acutal_day,Season
3/21/2020,Benito Juárez's Birthday Memorial,Saturday,3/21/2020,acutal_day,National holiday
4/5/2020,Palm Sunday,Sunday,4/5/2020,acutal_day,"Observance, Christian"
4/9/2020,Maundy Thursday,Thursday,4/9/2020,acutal_day,Bank holiday
4/10/2020,Good Friday,Friday,4/10/2020,acutal_day,Bank holiday
4/11/2020,Holy Saturday,Saturday,4/11/2020,acutal_day,Observance
4/12/2020,Easter Sunday,Sunday,4/12/2020,acutal_day,"Observance, Christian"
4/30/2020,Children's Day,Thursday,4/30/2020,acutal_day,Observance
5/1/2020,Labor Day / May Day,Friday,5/1/2020,acutal_day,National holiday
5/5/2020,Battle of Puebla (Cinco de Mayo),Tuesday,5/5/2020,acutal_day,Common local holiday
5/10/2020,Mother's Day,Sunday,5/10/2020,acutal_day,Observance
5/15/2020,Teacher's Day,Friday,5/15/2020,acutal_day,Observance
5/21/2020,Ascension Day,Thursday,5/21/2020,acutal_day,Observance
5/31/2020,Whit Sunday,Sunday,5/31/2020,acutal_day,Observance
6/11/2020,Corpus Christi,Thursday,6/11/2020,acutal_day,Observance
6/20/2020,June Solstice,Saturday,6/20/2020,acutal_day,Season
6/21/2020,Father's Day,Sunday,6/21/2020,acutal_day,Observance
8/15/2020,Assumption of Mary,Saturday,8/15/2020,acutal_day,Observance
9/15/2020,Shout of Dolores,Tuesday,9/15/2020,acutal_day,Observance
9/16/2020,Independence Day,Wednesday,9/16/2020,acutal_day,National holiday
9/22/2020,September Equinox,Tuesday,9/22/2020,acutal_day,Season
10/12/2020,Columbus Day,Monday,10/12/2020,acutal_day,Observance
10/31/2020,Halloween,Saturday,10/31/2020,acutal_day,Observance
11/1/2020,All Saints' Day,Sunday,11/1/2020,acutal_day,Observance
11/2/2020,All Souls' Day,Monday,11/2/2020,acutal_day,Observance
11/16/2020,Day off for Revolution Day Memorial,Monday,11/16/2020,acutal_day,National holiday
11/20/2020,Revolution Day Memorial,Friday,11/20/2020,acutal_day,National holiday
11/22/2020,Christ the King Day,Sunday,11/22/2020,acutal_day,Observance
12/8/2020,Feast of the Immaculate Conception,Tuesday,12/8/2020,acutal_day,Observance
12/12/2020,Day of the Virgin of Guadalupe,Saturday,12/12/2020,acutal_day,Bank holiday
12/21/2020,December Solstice,Monday,12/21/2020,acutal_day,Season
12/24/2020,Christmas Eve,Thursday,12/24/2020,acutal_day,"Observance, Christian"
12/25/2020,Christmas Day,Friday,12/25/2020,acutal_day,"National holiday, Christian"
12/28/2020,Day of the Holy Innocents,Monday,12/28/2020,acutal_day,Observance
12/31/2020,New Year's Eve,Thursday,12/31/2020,acutal_day,Observance
       """).to_pandas()


class MexicoPublicHolidayTransformer(CustomTransformer):
   @staticmethod
   def get_default_properties():
       return dict(col_type="date", min_cols=1, max_cols=1, relative_importance=1)

   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.time_column = self.input_feature_names[0]
       hdays = make_holiday_frame()['Observance']
       self.memo = pd.DataFrame(hdays, columns=[self.time_column], dtype='datetime64[ns]')
       self.memo['year'] = self.memo[self.time_column].dt.year
       self.memo['doy'] = self.memo[self.time_column].dt.dayofyear
       self.memo.sort_values(by=['year', 'doy']).drop_duplicates(subset=['year'], keep='first').reset_index(drop=True)
       self.memo.drop(self.time_column, axis=1, inplace=True)

   def fit_transform(self, X: dt.Frame, y: np.array = None):
       return self.transform(X)

   def transform(self, X: dt.Frame):
       X = X[:, self.time_column]
       if X[:, self.time_column].ltypes[0] != dt.ltype.str:
           assert self.datetime_formats[self.time_column] in ["%Y%m%d", "%Y%m%d%H%M"]
           X[:, self.time_column] = dt.stype.str32(dt.stype.int64(dt.f[0]))
       X.replace(['', 'None'], None)
       X = X.to_pandas()
       X.loc[:, self.time_column] = pd.to_datetime(X[self.time_column], format=self.datetime_formats[self.time_column])


       X['year'] = X[self.time_column].dt.year
       X['doy'] = X[self.time_column].dt.dayofyear
       X.drop(self.time_column, axis=1, inplace=True)
       feat = 'is_holiday'
       self.memo[feat] = 1
       X = X.merge(self.memo, how='left', on=['year', 'doy']).fillna(0)
       self.memo.drop(feat, axis=1, inplace=True)
       X = X[[feat]].astype(int)
       return X

