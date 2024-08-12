def inv_table(transition):
    invTrans = {}
    
    for state in transition.keys():
        invTrans[state] = {}
    
    for state, transitions in transition.items():
        for bit, next_state in transitions.items():
            invTrans[next_state][state] = bit
    
    return invTrans

def unshuffle(encFlag, transition):
    invTrans = inv_table(transition)
    current_state = 0
    decFlag = []
    
    for char in encFlag:
        next_state = int(char)
        original_bit = invTrans[next_state][current_state]
        decFlag.append(str(original_bit))
        current_state = next_state
    
    return ''.join(decFlag)

if __name__ == "__main__":
    transition = {
        0: {0: 7, 1: 3},
        1: {0: 4, 1: 9},
        2: {0: 6, 1: 8},
        3: {0: 1, 1: 5},
        4: {0: 9, 1: 0},
        5: {0: 8, 1: 2},
        6: {0: 0, 1: 7},
        7: {0: 5, 1: 1},
        8: {0: 2, 1: 6},
        9: {0: 3, 1: 4}
    }

    encFlag = "7140719494949358282603193582603586071403193193193586031493526752603582607194071935267582671493193528286075282671407194031940314075282607528603193586719494071931403140714031493586714949352671931403140319493582675286714940758603526758267194031935286752826031403149358671494075282671403140758603528607193149352671931935286752828603194031407140352828675867528603149403193586758607528675860319403586752867528286758603528603140358282607193582603586031493193528675260752828675860719407526719314935282826071931493586719494949352671403526714940752860314940319407193149494031407586758675267194071493586035867149407528603528603"  # replace this with the actual encrypted flag

    decFlag = unshuffle(encFlag, transition)
    print(f"binary Flag: {decFlag}")
    try:
        flag = bytes.fromhex(hex(int(decFlag, 2))[2:]).decode('utf-8')
        print(f"Flag: {flag}")
    except ValueError:
        print("Failed to decode flag. Ensure the binary flag is correct and represents valid ASCII.")
