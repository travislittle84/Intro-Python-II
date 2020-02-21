# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Player:
    def __init__(self, name, skill, bag = {}, current_room = [], disc_in_hand = None):
        self.skill = skill
        self.current_room = current_room
        self.bag = bag
        self.disc_in_hand = disc_in_hand
        self.skill_pct = self.skill / 100
        self.current_hole_shots = 0
        self.round_shots = 0
    
    def __str__(self):
        output = f'{self.name} on {self.current_room.name}'
        ats = dir(self)
        output += ats
        return output
    
    def setroom(self, room):
        self.current_room = room
        print(f'You are now in {self.current_room}!\n')

    def look(self):
        print(f"""{self.current_room.description} """)
    
    def look_intoBag(self):
        for disc in self.bag:
            print(f'{disc.name}')

    def set_disc_in_hand(self, disc):
        d = self.bag.get(disc)
        if d != None:
            self.disc_in_hand = d
            self.bag.pop(disc)
            print(f'You grab a {disc} from your bag...')
            return True
        else:
            print(f"You don't have a {disc} in your bag.")
            return False
    def remove_disc_from_hand(self, disc):
        self.disc_in_hand = None
        print("Removed disc from hand")

    def check_made_basket(self, target_dist, throw_dist, target_size):
        if target_dist - target_size <= throw_dist <= target_dist + target_size:
            self.round_shots += self.current_hole_shots
            return True
        else:
            return False

    def pickup_item(self, item):
        if item in self.current_room.items:
            self.bag[item] = self.current_room.items[item]
            self.current_room.items.pop(item)
            print(f'you picked up the {item} and put in your bag.')
        else:
            print(f'{item} is no where to be found...')
    
    def throw_disc(self, disc, target_dist):
        if self.disc_in_hand != None:
            # throw_dist = target - (target - skill) +  lower rnd(-target / 4 to target / 4 )
            max_disc_dist = self.disc_in_hand.max_distance
            self.current_hole_shots += 1
            throw_data = {
                'throw_distance': 0,
                'distance_to_pin': 0,
                'accuracy': 0,
                'in_basket': False,
                'is_ob': False
            }

            '''
            Determine if putting
                - If putting then as long as the disc is within 3ft then it's in
                - EX: target is 26 ft and player throws 24ft = in basket 
            If the target is 10 or less ft away from target then always make it

            If the target is 11-15 ft away then all players have 98% to make it

            if the target is 16-35 ft away then use shot accuracy to determine if putt is made

            if target is 36-50 ft

            '''
            if target_dist <= 50:
                # Putting mode
                print(f'50ft or less to pin, going for the putt...')

                if target_dist <= 10:
                    print(f'Tapped in the putt...')
                    throw_data["throw_distance"] = target_dist
                    throw_data["in_basket"] = True
                elif 10 <= target_dist <= 15:
                    throw_accuracy = random.randint(98, 100) / 100
                    throw_distance = round(target_dist * throw_accuracy)
                    
                    made_basket = self.check_made_basket(target_dist, throw_distance, 2)
                    if made_basket == True:
                        print(f'You made the {target_dist}ft putt!')
                        throw_data["throw_distance"] = target_dist
                        throw_data["in_basket"] = True
                    else:
                        print(f'You missed your {target_dist}ft putt :(')
                        dist_to_pin = abs(target_dist - throw_distance)
                        throw_data["throw_distance"] = throw_distance
                        throw_data["throw_accuracy"] = throw_accuracy
                        throw_data["distance_to_pin"] = dist_to_pin
                elif 16 <= target_dist <= 35:
                    throw_accuracy = random.randint(self.skill, 100) / 100
                    throw_distance = round(target_dist * throw_accuracy)

                    made_basket = self.check_made_basket(target_dist, throw_distance, 2)
                    if made_basket == True:
                        print(f'You made the {target_dist}ft putt!')
                        throw_data["throw_distance"] = target_dist
                        throw_data["in_basket"] = True
                    else:
                        print(f'You missed your {target_dist}ft putt :(')
                        dist_to_pin = abs(target_dist - throw_distance)
                        throw_data["throw_distance"] = throw_distance
                        throw_data["throw_accuracy"] = throw_accuracy
                        throw_data["distance_to_pin"] = dist_to_pin
                elif 36 <= target_dist <= 50:
                    throw_accuracy = random.randint(self.skill, 100) / 100
                    throw_distance = round(target_dist * throw_accuracy)

                    made_basket = self.check_made_basket(target_dist, throw_distance, 1)
                    if made_basket == True:
                        print(f'You made the {target_dist}ft putt!')
                        throw_data["throw_distance"] = target_dist
                        throw_data["in_basket"] = True
                    else:
                        print(f'You missed your {target_dist}ft putt :(')
                        dist_to_pin = abs(target_dist - throw_distance)
                        throw_data["throw_distance"] = throw_distance
                        throw_data["throw_accuracy"] = throw_accuracy
                        throw_data["distance_to_pin"] = dist_to_pin

            else:
                # Normal throwing mode
                throw_accuracy = random.randint(self.skill, 100) / 100

                # determine if the the target is further than the max disc distance
                # 
                # if the target is further than max disc dist OR using a DRIVER, then use max disc d
                # to calculate the throw distance. Otherwise use the target
                if target_dist > max_disc_dist or self.disc_in_hand.disc_type == 'driver':
                    throw_distance = round(max_disc_dist * throw_accuracy)
                else:
                    throw_distance = round(target_dist * throw_accuracy)
                
                made_basket = self.check_made_basket(target_dist, throw_distance, 1)
                if made_basket == True:
                    print(f'WOW! You threw it in from {target_dist}ft !')
                    throw_data["throw_distance"] = target_dist
                    throw_data["in_basket"] = True
                else:
                    print(f'You threw the disc {throw_distance}ft!')
                    dist_to_pin = abs(target_dist - throw_distance)
                    throw_data["throw_distance"] = throw_distance
                    throw_data["throw_accuracy"] = throw_accuracy
                    throw_data["distance_to_pin"] = dist_to_pin

            return throw_data
        else:
            print(f"You don't have a {disc} in your hand")
            return None

        


    

