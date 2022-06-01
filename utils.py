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
