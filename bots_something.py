
B = 'b'
O = 'o'

def calc_distance(destination, current):
    return abs(current - destination)

def is_same_bot(bota, botb):
    return bota is botb

def return_positive_or_zero(num):
    if num < 0:
        return 0
    return num

def run_bots(button_sequence):
    bots_position = {B: 1, O: 1}
    last_bot = None
    time = 0
    idle_time = 0

    for bot, next_position in button_sequence:
        distance = calc_distance(next_position, bots_position[bot])
        if not is_same_bot(last_bot, bot):
            distance = return_positive_or_zero(distance - idle_time)
            last_bot = bot
            idle_time = 0    
        time+= distance + 1
        idle_time+= distance + 1
        bots_position[bot] = next_position
    return time

        
