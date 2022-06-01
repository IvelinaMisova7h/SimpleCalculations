n = int(input())
w = float(input())
p = float(input())
m = int(input())
o = int(input())

the_whole_area = n * n
bench_area = m * o
area_with_tiles = the_whole_area - bench_area
tile_area = w * p

tiles_count = area_with_tiles / tile_area
time = tiles_count * 0.2

print(round(tiles_count, 2))
print(round(time, 2))

