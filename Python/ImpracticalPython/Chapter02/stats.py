import pstats
p = pstats.Stats('profile')
p.strip_dirs().sort_stats('cumulative').print_stats(10)