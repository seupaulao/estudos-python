import curses
from curses import wrapper

def carregartt():
    return [{"hora":"12:00:01","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:01","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:02","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:03","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:04","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:05","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:06","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:07","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},
{"hora":"12:00:08","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:09","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:10","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:11","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"V"},
{"hora":"12:00:11","qte":20,"valor":"2.700,22","comprador":"BTG","vendedor":"itau","agressor":"C"},]

def livroprecos():
    return [
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},
            {"qtec":20,"valorc":"2.700,50","valorv":"2.710,00","qtev":"50"},]



def testecor(agressor):
    if agressor=='V':
        return 1
    else: 
        return 2

def main(stdscr):

    stdscr.clear()
    cargatt=carregartt()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) 

    coltt = 35
    rowtt = 2
    n = 10
    for i in range(0, len(cargatt)):
        item=cargatt[i]
        stdscr.addstr(rowtt+i,coltt, '{}   {}  {}   {}   {}   {} '.format(item["hora"],item["qte"],item["valor"],item["comprador"],item["vendedor"],item["agressor"]),curses.color_pair(testecor(item["agressor"])))

    collp=2
    boleta = livroprecos()
    for i in range(0, len(boleta)):
        item = boleta[i]
        stdscr.addstr(rowtt+i,collp, '{}    {}    {}    {}'.format(item['qtec'],item['valorc'],item['valorv'],item['qtev']))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

