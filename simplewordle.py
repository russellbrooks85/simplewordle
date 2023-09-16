import tkinter as tk
import random
from tkinter import messagebox
from itertools import repeat

alphabet_left = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
alphabet_color = []

attempts=6
guess="_____"
#List of five-letter words to choose from
word_list = ["ABACK","ABASE","ABATE","ABBEY","ABOUT","ABOVE","ABYSS","ACRID","ACUTE","ADMIT","ADOBE","ADOPT","ADORE","AGAIN","AGAPE","AGATE","AGILE","AGLOW","AGONY","AGREE","AHEAD","ALBUM","ALIEN","ALIKE","ALLOW","ALOFT","ALONE","ALOUD","ALPHA","ALTAR","ALTER","AMBER","AMISS","AMPLE","ANGER","ANGRY","ANODE","ANTIC","AORTA","APHID","APPLE","APPLY","APRON","APTLY","ARBOR","ARGUE","AROMA","ASIDE","ASKEW","ASSET","ATOLL","ATONE","AUDIO","AUDIT","AVAIL","AVERT","AWAIT","AWAKE","AWFUL","AXIOM","BADGE","BADLY","BAGEL","BAKER","BALSA","BANAL","BARGE","BASIC","BATHE","BATON","BATTY","BAYOU","BEACH","BEADY","BEAST","BEEFY","BEGET","BEGIN","BEING","BELCH","BELIE","BELLY","BELOW","BENCH","BERTH","BESET","BIOME","BIRCH","BIRTH","BLACK","BLAME","BLAND","BLEED","BLEEP","BLOKE","BLOWN","BLUFF","BLURB","BLURT","BLUSH","BOOBY","BOOST","BOOZE","BOOZY","BORAX","BOUGH","BRAID","BRAKE","BRASH","BRAVE","BREAD","BREAK","BRIAR","BRIBE","BRIDE","BRINE","BRING","BRINK","BRISK","BROKE","BROOK","BROOM","BUGGY","BULLY","BURLY","CACAO","CACHE","CANNY","CANOE","CAPER","CARAT","CARGO","CARRY","CATCH","CATER","CAULK","CEDAR","CHAFE","CHAMP","CHANT","CHARD","CHARM","CHART","CHEAT","CHEEK","CHEST","CHIEF","CHILL","CHOIR","CHOKE","CHORD","CHUNK","CHUTE","CIDER","CIGAR","CINCH","CIRCA","CIVIC","CLASS","CLEAN","CLEAR","CLERK","CLICK","CLING","CLOCK","CLOTH","CLOWN","CLUCK","COAST","COCOA","COLON","COMET","COMMA","CONDO","CONIC","CORNY","COULD","COUNT","COVET","COWER","COYLY","CRAMP","CRANE","CRANK","CRASS","CRATE","CRAVE","CRAZE","CRAZY","CREAK","CREDO","CREPT","CRIME","CRIMP","CROAK","CRONE","CROSS","CRUMB","CRUST","CURLY","CYNIC","DANCE","DANDY","DEATH","DEBUG","DELTA","DELVE","DENIM","DEPOT","DEPTH","DIGIT","DINER","DISCO","DITTO","DODGE","DONOR","DONUT","DOUBT","DOWRY","DOZEN","DRAIN","DREAM","DRINK","DRIVE","DROLL","DROOP","DUCHY","DUTCH","DUVET","DWARF","DWELL","DWELT","EARTH","EGRET","EJECT","ELDER","ELOPE","ELUDE","EMAIL","EMPTY","ENEMA","ENJOY","ENNUI","ENTER","EPOCH","EPOXY","EQUAL","ERODE","ERROR","ESSAY","ETHIC","ETHOS","EVADE","EVERY","EXACT","EXCEL","EXERT","EXIST","EXTRA","EXULT","FARCE","FAULT","FAVOR","FEAST","FEIGN","FERRY","FEWER","FIELD","FIEND","FIFTY","FINER","FIRST","FISHY","FIXER","FJORD","FLAIL","FLAIR","FLANK","FLASK","FLESH","FLICK","FLING","FLIRT","FLOAT","FLOCK","FLOOD","FLOOR","FLORA","FLOSS","FLOUT","FLUFF","FLUME","FLYER","FOCAL","FOCUS","FOGGY","FOLLY","FORAY","FORGE","FORGO","FORTH","FOUND","FOYER","FRAME","FRESH","FROCK","FRONT","FROST","FROTH","FROZE","FUNGI","GAMER","GAMMA","GAUDY","GAUZE","GAWKY","GECKO","GHOUL","GIANT","GIDDY","GIRTH","GLASS","GLEAN","GLOAT","GLOOM","GLORY","GLOVE","GLYPH","GNASH","GOLEM","GONER","GOOSE","GORGE","GOUGE","GRADE","GRAND","GRATE","GREAT","GREET","GRIEF","GRIME","GRIMY","GRIPE","GROIN","GROUP","GROUT","GROVE","GROWL","GRUEL","GUANO","GUARD","GUEST","GUILD","GULLY","GUPPY","HAIRY","HAPPY","HATCH","HATER","HAVOC","HEADY","HEART","HEATH","HEIST","HELIX","HELLO","HERON","HINGE","HOARD","HOBBY","HOMER","HORDE","HORSE","HOTEL","HOUND","HOWDY","HUMAN","HUMID","HUMOR","HUMPH","HUNKY","HURRY","HUTCH","HYPER","IGLOO","IMPEL","INANE","INDEX","INEPT","INERT","INFER","INPUT","INTER","IONIC","IRATE","IRONY","ISLET","ITCHY","IVORY","JAUNT","JAZZY","JOKER","JOUST","JUDGE","KARMA","KAYAK","KAZOO","KEBAB","KHAKI","KIOSK","KNEEL","KNOCK","KNOLL","KOALA","LABEL","LABOR","LAPEL","LAPSE","LARVA","LATTE","LAYER","LEAFY","LEAPT","LEAVE","LEDGE","LEERY","LEMON","LIBEL","LIGHT","LILAC","LINEN","LIVER","LOCUS","LOFTY","LOGIC","LOOPY","LOSER","LOVER","LOWLY","LUCKY","LUNAR","LUSTY","LYING","MADAM","MAGIC","MAGMA","MAIZE","MAJOR","MANLY","MANOR","MAPLE","MARCH","MARRY","MARSH","MASSE","MATEY","MAXIM","MAYBE","MEALY","MEDAL","MERIT","METAL","METRO","MIDGE","MIDST","MIMIC","MINCE","MODEL","MOIST","MOLAR","MONEY","MONTH","MOOSE","MOSSY","MOTOR","MOTTO","MOULT","MOUNT","MOURN","MOUSE","MOVIE","MUCKY","MUMMY","NAIVE","NANNY","NASTY","NATAL","NAVAL","NEEDY","NIGHT","NINTH","NYMPH","OCEAN","OFFAL","OLDER","OLIVE","ONION","ONSET","OPERA","OTHER","OUGHT","OUTDO","OXIDE","PANEL","PANIC","PAPER","PARER","PARRY","PARTY","PATTY","PAUSE","PEACE","PEACH","PERCH","PERKY","PHASE","PHOTO","PICKY","PIETY","PILOT","PINEY","PINKY","PINTO","PITHY","PIXIE","PLANK","PLANT","PLATE","PLAZA","PLEAT","PLUCK","PLUNK","POINT","POISE","POKER","POLKA","POLYP","POUND","POWER","PRICK","PRIDE","PRIME","PRIMO","PRINT","PRIZE","PROBE","PROVE","PROXY","PULPY","PURGE","QUALM","QUART","QUERY","QUEST","QUICK","QUIET","QUIRK","QUOTE","RADIO","RAINY","RAMEN","RANCH","RANGE","RATIO","RAYON","REACT","REBUS","REBUT","RECAP","REGAL","RENEW","REPAY","RETCH","RETRO","REVEL","RHINO","RHYME","RIPER","RIVAL","ROBIN","ROBOT","RODEO","ROGUE","ROOMY","ROUGE","ROUND","ROUSE","ROYAL","RUDDY","RUDER","RUPEE","RUSTY","SAINT","SALAD","SALSA","SAUTE","SCALD","SCARE","SCARF","SCOLD","SCORN","SCOUR","SCOUT","SCRAP","SCRUB","SEDAN","SEEDY","SERVE","SEVER","SHAKE","SHALL","SHAME","SHARD","SHAWL","SHINE","SHIRE","SHIRK","SHORN","SHOWN","SHOWY","SHRUB","SHRUG","SHYLY","SIEGE","SISSY","SKILL","SKIMP","SKIRT","SLATE","SLEEK","SLOSH","SLOTH","SLUMP","SLUNG","SMART","SMASH","SMEAR","SMELT","SMITE","SNACK","SNAFU","SNAKY","SNARL","SNEAK","SNOUT","SOGGY","SOLAR","SOLVE","SONIC","SOUND","SOWER","SPACE","SPADE","SPELL","SPEND","SPICE","SPICY","SPIEL","SPIKE","SPILL","SPIRE","SPOKE","SPRAY","SQUAD","SQUAT","STAFF","STAGE","STAID","STAIR","STALE","STAND","START","STEAD","STEED","STEIN","STICK","STING","STINK","STOCK","STOMP","STOOL","STORE","STORY","STOUT","STOVE","STRAP","STRAW","STUDY","STYLE","SUGAR","SULKY","SURER","SURLY","SWEAT","SWEEP","SWEET","SWILL","SWINE","SWIRL","SYRUP","TACIT","TANGY","TAPER","TAPIR","TASTE","TASTY","TAUNT","TEASE","TENTH","TEPID","THEIR","THEME","THERE","THIEF","THIRD","THORN","THOSE","THUMB","THUMP","THYME","TIARA","TIBIA","TIGER","TILDE","TIPSY","TODAY","TONIC","TOPAZ","TORSO","TOTEM","TOUGH","TOXIC","TRACE","TRACT","TRAIN","TRAIT","TRASH","TRAWL","TREAT","TREND","TRIAD","TRICE","TRITE","TROLL","TROPE","TROVE","TRUSS","TRYST","TWANG","TWEED","TWICE","TWINE","ULCER","ULTRA","UNDER","UNDUE","UNFED","UNFIT","UNIFY","UNITE","UNLIT","UNMET","UNTIE","UNZIP","UPSET","USAGE","USHER","USING","USUAL","USURP","UTTER","VAGUE","VALET","VALID","VENOM","VERVE","VIGOR","VIRAL","VITAL","VIVID","VODKA","VOICE","VOTER","VOUCH","WACKY","WALTZ","WASTE","WATCH","WEARY","WEDGE","WHACK","WHALE","WHEEL","WHELP","WHERE","WHIFF","WHINE","WHIRL","WHISK","WHOOP","WINCE","WINDY","WOKEN","WOOER","WORDY","WORLD","WORRY","WORSE","WOVEN","WRATH","WRITE","WRONG","WROTE","WRUNG","YACHT","YEARN","YIELD","YOUTH","ZESTY"]

# Initialize the game
def initialize_game():
    global secret_word, attempts,alphabet_left,alphabet_color
    secret_word = random.choice(word_list)
    attempts = 6
    alphabet_left = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    alphabet_color = []
    alphabet_color.extend(repeat("gray",27))
    #print(len(alphabet_color),alphabet_color)
    canvas_feedback.delete("all")
    update_display(guess, attempts,alphabet_left,alphabet_color)

# Check the guess and update the display
def check_guess():
    global attempts
    guess = entry_guess.get().upper()
    #print(guess, attempts)
    if len(guess) != 5 or not guess.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a valid 5-letter word.")
        return
    
    attempts -= 1
    update_display(guess, attempts,alphabet_left,alphabet_color)

    if guess == secret_word:
        messagebox.showinfo("Congratulations!", "You guessed the word correctly.")
        initialize_game()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"Out of attempts. The word was '{secret_word}'.")
        initialize_game()

# Update the display with the current state
def update_display(guess, attempts,alphabet_left,alphabet_color ):
    label_attempts.config(text=f"Attempts left: {attempts}")
    entry_guess.delete(0, tk.END)
    #canvas_feedback.delete("all")
    att = attempts
    if att>5:
        att=5
    for i in range(5):
        if secret_word[i] == guess[i]:
            color = "green"
        elif guess[i] in secret_word:
            color = "yellow"
        else:
            color = "gray"
        #print(i * 40, ((5-att)*40), (i + 1) * 40, 40+((5-att)*40))
        #print(i * 40 + 20, 20+((5-att)*40))
        canvas_feedback.create_rectangle(i * 40+100, ((5-att)*40), (i + 1) * 40+100, 40+((5-att)*40), fill=color, outline="")
        canvas_feedback.create_text(i * 40 + 20+100, 20+((5-att)*40), text=guess[i], font=("Helvetica", 16))

    for i in range(0,len(guess)):
        for u in range(0,len(alphabet_left)):
            if guess[i].upper() == alphabet_left[u]:
                alphabet_left[u] = '_'
                alphabet_color[u]="black"
                #print(u,alphabet_color[u])
    for u in range(0,10):
        canvas_feedback.create_rectangle(u * 40, 300+(40), (u + 1) * 40, 300+40+(40), fill=alphabet_color[u], outline="")
        canvas_feedback.create_text(u * 40 + 20, 300+20+(40), text=alphabet_left[u], font=("Helvetica", 16))
    for u in range(10,19):
        canvas_feedback.create_rectangle((u-9.5) * 40, 340+(40), ((u-9.5) + 1) * 40, 340+40+(40), fill=alphabet_color[u], outline="")
        canvas_feedback.create_text((u-9.5) * 40 + 20, 340+20+(40), text=alphabet_left[u], font=("Helvetica", 16))
    for u in range(19,26):
        canvas_feedback.create_rectangle((u-18) * 40, 380+(40), ((u-18) + 1) * 40, 380+40+(40), fill=alphabet_color[u], outline="")
        canvas_feedback.create_text((u-18) * 40 + 20, 380+20+(40), text=alphabet_left[u], font=("Helvetica", 16))



     


    

# Create the main window

window = tk.Tk()
window.title("Wordle Game")
# Widgets
label_attempts = tk.Label(window, text=f"Attempts left: {attempts}")
entry_guess = tk.Entry(window, width=10)
button_guess = tk.Button(window, text="Guess", command=check_guess)
canvas_feedback = tk.Canvas(window, width=400, height=500)


# Layout
label_attempts.pack()
entry_guess.pack()
button_guess.pack()
canvas_feedback.pack()



# Initialize the game
initialize_game()
# Start the GUI main loop
window.mainloop()
