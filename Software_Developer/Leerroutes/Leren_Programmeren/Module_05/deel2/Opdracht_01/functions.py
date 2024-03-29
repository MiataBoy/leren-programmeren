import math
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, \
    COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY, COST_INN_HORSE_COPPER_PER_NIGHT, COST_INN_HUMAN_SILVER_PER_NIGHT


##################### M04.D02.O2 #####################

def copper2silver(amount: int) -> float:
    return amount / 10


def silver2gold(amount: int) -> float:
    return amount / 5


def copper2gold(amount: int) -> float:
    silver = copper2silver(amount)
    return silver2gold(silver)


def platinum2gold(amount: int) -> float:
    return amount * 25


def getPersonCashInGold(personCash: dict) -> float:
    gold = personCash['gold']
    gold += copper2gold(personCash['copper'])
    gold += silver2gold(personCash['silver'])
    gold += platinum2gold(personCash['platinum'])
    return gold


##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    copperCosts = JOURNEY_IN_DAYS * (people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    gold = copper2gold(copperCosts)
    copperCosts = JOURNEY_IN_DAYS * (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    gold += copper2gold(copperCosts)
    return round(gold, 2)


##################### M04.D02.O5 #####################

def getFromListByKeyIs(list: list, key: str, value: any) -> list:
    listing = []
    for x in list:
        if x[key] == value:
            listing.append(x)
    return listing


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends: list) -> list:  # Hier stond eerst int, klopte dit?
    return getFromListByKeyIs(friends, "shareWith", True)


def getAdventuringFriends(friends: list) -> list:
    listing = []
    adv = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)
    for x in adv:
        if x['adventuring'] and x['shareWith'] and x not in listing:
            listing.append(x)
    for y in share:
        if y['adventuring'] and y['shareWith'] and y not in listing:
            listing.append(y)
    return listing


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)


def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)


def getTotalRentalCost(horses: int, tents: int) -> float:
    tenties = math.ceil(JOURNEY_IN_DAYS / 7) * (tents * COST_TENT_GOLD_PER_WEEK)
    horsies = horses * (JOURNEY_IN_DAYS * COST_HORSE_SILVER_PER_DAY)
    return tenties + silver2gold(horsies)


##################### M04.D02.O7 #####################

def getItemsAsText(items: list) -> str:
    itemText = []
    for item in items:
        itemText.append(f"{item['amount']}{item['unit']} {item['name']}")
    return ', '.join(itemText)


def getItemsValueInGold(items: list) -> float:
    value = float()
    for item in items:
        amount = item['amount']
        pricetype = item['price']['type']
        price = item['price']['amount']

        if pricetype == 'copper':
            value += amount * copper2gold(price)
        elif pricetype == 'silver':
            value += amount * silver2gold(price)
        elif pricetype == 'platinum':
            value += amount * platinum2gold(price)
        else:
            value += amount * price
    return value


##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total = 0
    for person in people:
        total += person['cash']['gold']
        total += platinum2gold(person['cash']['platinum'])
        total += silver2gold(person['cash']['silver'])
        total += copper2gold(person['cash']['copper'])
    return total

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors: list) -> list:
    interestingInvestor = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            interestingInvestor.append(investor)
    return interestingInvestor

def getAdventuringInvestors(investors: list) -> list:
    investors = getInterestingInvestors(investors)
    adventuringInvestor = []
    for investor in investors:
        if investor['adventuring']:
            adventuringInvestor.append(investor)
    return adventuringInvestor


def getTotalInvestorsCosts(investors: list, gear: list) -> float:

    gold = 0
    investors = getAdventuringInvestors(investors)
    for investor in range(len(investors)):
        gold += getItemsValueInGold(gear)
        #print("itemsvalueingold: ", getItemsValueInGold(gear))
    gold += getJourneyFoodCostsInGold(len(investors), len(investors))
    gold += getTotalRentalCost(len(investors), len(investors))
    # print("totalrentalcost: ", getTotalRentalCost(len(investors), len(investors)))
    # print("journeyfoodcosts: ", getJourneyFoodCostsInGold(len(investors), len(investors)))
    print(gold)
    return gold

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    humanCost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horseCost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold/(horseCost+humanCost))


def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    human_per_night_Gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_per_night_Gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return round((human_per_night_Gold + horses_per_night_Gold) * nightsInInn, 2)


##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold: float, investors: list) -> list:
    cuts = []
    investors = getInterestingInvestors(investors)
    for investor in investors:
        cuts.append(round(investor['profitReturn'] / 100 * profitGold, 2))
    return cuts


def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    totalCut = 0
    for cut in investorsCuts:
        totalCut += cut
    return round((profitGold - totalCut) / fellowship, 2)
    # fellowship moet je alleen de hoeveelheid mensen berekenen, tenzij in testen veranderd


##################### M04.D02.O13 #####################

def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(interestingInvestors)
    investorsCuts = getInvestorsCuts(profitGold, interestingInvestors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(adventuringFriends) + len(adventuringInvestors) + 1)

    # verdeel de uitkomsten
    for person in people:
        # code aanvullen
        startGold = getPersonCashInGold(person['cash'])
        endGold = startGold

        if person == mainCharacter:
            endGold += goldCut + round(len(adventuringFriends)*10,2)
        elif person in adventuringInvestors:
            endGold += goldCut
        elif person in adventuringFriends:
            endGold += goldCut - 10
        if person in interestingInvestors:
            endGold += round(profitGold * person['profitReturn'] / 100, 2)

        earnings.append({
            'name': person['name'],
            'start': round(startGold,2),
            'end': round(endGold,2)
        })

    return earnings

##################### view functions #####################
def print_colorvars(txt: str = '{}', vars: list = [], color: str = 'yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']), vars)
    print(txt.format(*vars))


def print_title(name: str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')


def print_chapter(number: int, name: str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')


def nextStep(secwait: int = 1) -> None:
    print('')
    time.sleep(secwait)


def ifOne(amount: int, yes: str, no: str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
