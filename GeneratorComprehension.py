# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [row[11:19] for row in tweet_time if row[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
