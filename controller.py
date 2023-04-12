import view
import text_fields as tx
from classes import MainClass

def start_td():
    while True:
        choice = view.main_menu()
        cl = MainClass('tel_directory.txt')
        match choice:
            case 1:
                cl.calc_lenght()          #  Теперь переходим к КЛАССУ !!!
                td = cl.load_file()
                view.show_dir(td, cl.max_l)
                view.print_mes('', 1)
            case 2:
                dat = view.enter_cont()
                cl.create_contact(dat)
                view.print_mes(tx.add_contact, 1)
            case 3:
                st = view.enter_find_str()
                cl.calc_lenght()     # здесь получится грубое форматирование (по максимальной длине, но в списке поиска этих величин может и не быть)
                fl = cl.find_contact(st)
                view.print_mes(tx.find_not_null, 0)
                view.show_dir(fl, cl.max_l)
                view.print_mes('', 1)
            case 4:
                td = cl.load_file()
                cl.calc_lenght()
                view.show_dir(td, cl.max_l)
                nom = view.enter_numb()
                view.print_mes(str(td[nom-1][0]) + '. ' + td[nom-1][1], 0)
                cord = view.enter_edit_contact()
                cl.edit_contact(td, nom, cord)
                view.print_mes(tx.edit_succes, 1)
            case 5:
                td = cl.load_file()
                cl.calc_lenght()
                view.show_dir(td, cl.max_l)
                nom = view.enter_numb()
                cl.delete_contact(td, nom)
                view.print_mes(tx.del_succes, 1)
            case 6:
                view.print_mes(tx.bye_bye, 0)
                exit()



