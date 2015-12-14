show_views_file = sc.textFile("input_join2/join2_gennum?.txt")
# [u'Hourly_Sports,21']

show_views = show_views_file.Map(split_show_views)
# [(u'Hourly_Sports', u'21')]

show_channel_file = sc.textFile("input_join2/join2_genchan?.txt")
# [u'Hourly_Sports,DEF']

show_channel = show_channel_file.map(split_show_channel)
# [(u'Hourly_Sports', u'DEF')]

joined_dataset = show_channel.join(show_views)
# [(u'PostModern_Cooking', (u'DEF', u'1038'))]

channel_views = joined_dataset.map(extract_channel_view)
# [(u'DEF', u'1038')]

channel_views.reduceByKey(sum).collect()
# (u'BAT', 5099141)
