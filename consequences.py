"""
https://flood-warning-information.service.gov.uk/station/8208

Riverside path on the Joseph Rowntree Park side of the river > 2.9m and < 3.3m Exact level not known at this time

"""
import collections
import sys

nodes = {
    'BRG': 'Bridge',
    'NEW': 'New Walk',
    'TAV': 'Terry Avenue',
    'HFR': 'Hospital Fields Road',
    'MAG': 'Maple Grove',
    'BTR': 'Butcher Terrace'
}

infos = {
    ('BRG', 'NEW'): { 2.4: 'Unsure',
                      2.9: 'BLOCKED'},
    ('BRG', 'HFR'): { 3.5: 'Unsure',
                      3.6: 'Just passable on foot and bike',
                      3.7: 'Unsure',
                      4.0: 'Passable by bike, water nearly up to kerbstones.'},
    ('BRG', 'BTR'): { 3.8: 'Unsure',
                      4.0: 'Not recommended. Puddle across path deep enough to foul the crank. Possible for pedestrians to get round it on ,waterlogged grass.',
                      4.1: 'BLOCKED'},
    ('BRG', 'MAG'): { 4.3: 'Unsure. But the bridge is unusable on the other side'},
    ('BRG', 'TAV'): { 2.9: 'Unsure',
                      3.3: 'BLOCKED' }
}

def generate_possible_routes( nodes ):
    for i, src in enumerate(node_names):
        for dst in node_names[i+1:]:
            yield( (src,dst) )

def get_deepest_trigger( triggers, depth):
    last_trigger=0
    last_message=None

    for trigger_depth, message in triggers.items():
        if trigger_depth > last_trigger and depth >= trigger_depth:
            last_trigger=trigger_depth
            last_message = message
    return last_trigger, last_message
    
def get_statuses( depth ):
    """ generate a list of the depth statuses that are triggered for each route.  
        Only the deepest trigger is returned for each route. """
    for key in infos.keys():
        alerts = infos[key]
        trigger =get_deepest_trigger(alerts, depth)
        if trigger[1]:
            yield key, trigger
        
if __name__ == "__main__":
    depth = float(sys.argv[1])

    node_names = list(nodes.keys())
    possible_routes = list(generate_possible_routes(nodes.keys()))

    updates = list(get_statuses( depth ))

    for (src,dst), (dep, msg) in updates:
        print(f'{nodes[src]} to {nodes[dst]}: {depth-dep:0.2f}m above status: {msg} ')

