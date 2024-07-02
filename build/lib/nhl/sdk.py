from .services.player import PlayerService
from .services.skater_stats import SkaterStatsService
from .services.goalie_stats import GoalieStatsService
from .services.player_spotlight import PlayerSpotlightService
from .services.standings import StandingsService
from .services.club_stats import ClubStatsService
from .services.scoreboard import ScoreboardService
from .services.roster import RosterService
from .services.schedule import ScheduleService
from .net.environment import Environment

class Nhl:
    def __init__(self,base_url: str = Environment.DEFAULT.value):
        """
        Initializes Nhl the SDK class.
        """
        self.player = PlayerService(base_url=base_url)
        self.skater_stats = SkaterStatsService(base_url=base_url)
        self.goalie_stats = GoalieStatsService(base_url=base_url)
        self.player_spotlight = PlayerSpotlightService(base_url=base_url)
        self.standings = StandingsService(base_url=base_url)
        self.club_stats = ClubStatsService(base_url=base_url)
        self.scoreboard = ScoreboardService(base_url=base_url)
        self.roster = RosterService(base_url=base_url)
        self.schedule = ScheduleService(base_url=base_url)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.player.set_base_url(base_url)
        self.skater_stats.set_base_url(base_url)
        self.goalie_stats.set_base_url(base_url)
        self.player_spotlight.set_base_url(base_url)
        self.standings.set_base_url(base_url)
        self.club_stats.set_base_url(base_url)
        self.scoreboard.set_base_url(base_url)
        self.roster.set_base_url(base_url)
        self.schedule.set_base_url(base_url)

        return self









# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c

