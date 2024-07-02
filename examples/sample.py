from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.skater_stats.get_current_skater_stats_leaders(
    categories="categories",
    limit=2
)

print(result)

