def TraderInteraction(game, option, region):
    if game.player.credits > option.credits:
        game.buy(option.item)
    elif ignores:
        travel to region
    elif (canRob) {
        if (isAbleToWin) {
            stealItem()
        } else {
            damageShipHealth
        }
    } else if (wantsToNegotiate) {
        if (canNegotiate) {
            buyReducedPrice()
        } else {
            if (wantsToBuy) {
                buyHighPrice()
            } else {
                if (wantsToBuy) {
                    buy()
                } else if (ignores) {
                    ignore()
                } else {
                    rob()
                }
            }
        }
    }