def strip_year(x):
    return re.sub(r'[^a-zA-Z]', '', str(x))

def date_parse(x, date_format=None):
    if date_format is None:
        date_format =  "%Y-%m-%d"                              # use suitable dateformat depending on context
    return datetime.strptime(str(x), date_format)

def find_null_perc(df):
    result = df.isnull().sum()*100/df.shape[0]
    print(result)

def get_top_factors(factor_series, thresh=None):               # For a categorical attribute, retrieve the set of values which are atleast thresh% in support.
    if thresh is None:
        thresh = 1
    factor_counts = factor_series.value_counts()
    top_factors = factor_counts[factor_counts*100/df.shape[0] >= thresh].index
    return top_factors

def apply_multiple_aggs_across_cols(x):
    d = dict()
    # Idea is to create a dictionary, where each key corresponds to a particular aggregation on the pd.DataFrameGroupBy object (grouped df)
    # The value for the corresponding key can be calculated as required, columns can be accessed treated x as a normal df, 
    # but explicit aggregation has to occur on the grouped object
    
    d['agg1] = x['col1'].count()  
    d['agg2'] = (x['col2'] * x['col3']).sum()
    # ... etc
    
    return pd.Series(d)

def plot_figure(X, Y, x_axis, y_axis, title, shape=(8,5), marker='ro'):
    plt.figure(figsize=shape)
    plt.plot(X, Y,marker)
    plt.ylabel(y_axis)
    plt.xlabel(x_axis)
    plt.title(title)
    plt.show()

def plot_multiple_graphs(df, iterable):
      ''' This function is to plot multiple graphs in the same figure. I have achieved this in many ways in my work experience, but I always had to look up docs,
      or stack-overflow, etc and revisit this logic. This is an attempt to use this function out of the box, for a generic use-case. 
      Please feel free to use this/reach out to me for any suggestions/improvements'''
      
      # iterable contains multiple values, each for which a subplot has to be plotted in the figure. 
      # Lets take iterable to be the list ['India', 'China', 'US', 'Japan', 'Russia', 'UAE']
      # Lets assume that there is a 'country' column in the df with which the df can be sliced accordingly relevant to the above list.
      # Lets also assume that there is a 'GDP' column and a 'year' column in the dataset. We will use these to form our graphs for the six countries
      
 
      x=2, y=3                                                                  # Initializing layout parameters: ideally x*y = len(iterable)
      fig, ax = plt.subplots(x, y, sharex='col', sharey='row', figsize=(20,10)) #(additional parameters to plt.figure can be passed here!)
      fig.subplots_adjust(hspace=0.4, wspace=0.4)                               # If you want spacing between subplots. DONT use with tight_layout()

      # axes are in a two-dimensional array, indexed by [row, col]
      for i in range(x):
          for j in range(y):
              country = iterable[x*i + j]                    # NOTE: subplots starts indexing from 0, so it can be directly used in our iterable
              country_df = df[df['country'] == country]      # Getting the slice of the country
              X = country_df['year']
              Y = country_df['GDP']
              ax[i, j].plot(X, Y)                            # Additional paramters to plot() can be passed here!
              ax[i, j].set_title(country)                    # Set title for each indvidual subplot
              ax[i, j].set_xlabel('year')                    # Set xlabel for each indvidual subplot
              ax[i, j].set_ylabel('GDP')                     # Set ylabel for each indvidual subplot
      fig.tight_layout()                                     # If you don't want any white space between plots. DONT use with subplots_adjust()
