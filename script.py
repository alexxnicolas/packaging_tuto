import biketrauma

df = biketrauma.Load_db().save_as_df()
#biketrauma.plot_location(biketrauma.get_accident(df))
df_nicely_formated = biketrauma.format_date(df)