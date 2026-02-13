def statistics_calculation_output(y):
    
    min_df = round(y.min(),2)
    median_df = round(y.median(),2)
    mean_df = round(y.mean(),2)
    max_df = round(y.max(),2)
    range_max_min_df = round(y.max()-y.min(),2)

    std_df = round(y.std(),2)
    q1_df = round(y.quantile(0.25),2)
    q2_df = round(y.quantile(0.50),2)
    q3_df = round(y.quantile(0.75),2)
    amount_df = y.count()
    return min_df,median_df,mean_df,max_df,range_max_min_df,std_df,q1_df,q2_df,q3_df,amount_df
