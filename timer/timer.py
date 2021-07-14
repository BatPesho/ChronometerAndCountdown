from threading import *
from datetime import *
another_device = True
global choice
chrono_threads = []
countdown_threads = []
from beepy import beep
from time import sleep

a = -1
b= -1

class Countdown(Thread):

    stop_countdown = True

    def stop(self):
        self.stop_countdown = False
        print("Countdown ended before finishing")

    def run(self):
        date_str = "\r\n"+"{0}/{1}/{2} {3}:{4}:{5}"
        thread1_seconds = seconds
        thread1_minutes = minutes
        thread1_hours = hours
        thread1_days = day
        thread1_months = month
        thread1_years = year

        thread1_end_seconds = seconds1
        thread1_end_minutes = minutes1
        thread1_end_hours = hours1
        thread1_end_days = day1
        thread1_end_months = month1
        thread1_end_years = year1
        #print("End Date")
        #print(thread1_end_seconds, thread1_end_minutes, thread1_end_hours, thread1_end_days, thread1_end_months, thread1_end_years)

        while stop_countdown:
            if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days ==  thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                break
            """
            if thread1_seconds > 10 and thread1_minutes > 10 and thread1_hours > 10:
                date_str = "{0}/{1}/{2} {3}:{4}:{5}"
            elif thread1_seconds < 10 and thread1_minutes < 10 and thread1_hours < 10:
                date_str = "{0}/{1}/{2} 0{3}:0{4}:0{5}"
            elif thread1_seconds < 10 and thread1_minutes < 10 and thread1_hours > 10:
                date_str = "{0}/{1}/{2} {3}:0{4}:0{5}"
            elif thread1_seconds < 10 and thread1_minutes > 10 and thread1_hours > 10:
                date_str = "{0}/{1}/{2} {3}:{4}:0{5}"
            elif thread1_seconds > 10 and thread1_minutes < 10 and thread1_hours > 10:
                date_str = "{0}/{1}/{2} {3}:0{4}:{5}"
            elif thread1_seconds > 10 and thread1_minutes < 10 and thread1_hours < 10:
                date_str = "{0}/{1}/{2} 0{3}:0{4}:{5}"
            elif thread1_seconds > 10 and thread1_minutes > 10 and thread1_hours < 10:
                date_str = "{0}/{1}/{2} 0{3}:{4}:{5}"
            """


           # print(date_str.format(thread1_years, thread1_months, thread1_days, thread1_hours, thread1_minutes, thread1_seconds))
            #print("End")
            #print(thread1_end_seconds, thread1_end_minutes, thread1_end_hours, thread1_end_days, thread1_end_months,
            #     thread1_end_years)
            sleep(1)
            if thread1_seconds > 0:
                thread1_seconds -= 1

            if thread1_seconds == 0:
             #   print("Current")
            #    print(date_str.format(thread1_years, thread1_months, thread1_days, thread1_hours, thread1_minutes, thread1_seconds))
                if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days == thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                    break
                thread1_minutes -= 1
                sleep(1)
                thread1_seconds = 59
            else:
                if thread1_minutes == 0:
                    if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days == thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                        break
                    thread1_hours -= 1

                    thread1_minutes = 59
                else:
                    if thread1_hours == 0:
                        if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days == thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                            break
                        thread1_days -= 1
                        thread1_hours = 23
                    else:
                        if thread1_days == 0:
                            if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days == thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                                break
                            thread1_months -= 1
                            if thread1_months == 12:
                                thread1_days = 31
                            elif thread1_months == 11:
                                thread1_days = 30
                            elif thread1_months == 10:
                                thread1_days = 31
                            elif thread1_months == 9:
                                thread1_days = 30
                            elif thread1_months == 8:
                                thread1_days = 31
                            elif thread1_months == 7:
                                thread1_days = 31
                            elif thread1_months == 6:
                                thread1_days = 30
                            elif thread1_months == 5:
                                thread1_days = 31
                            elif thread1_months == 4:
                                thread1_days = 30
                            elif thread1_months == 3:
                                thread1_days = 31
                            elif thread1_months == 2:
                                thread1_days = 28
                            elif thread1_months == 1:
                                thread1_days = 31
                            else:
                                if thread1_seconds == thread1_end_seconds and thread1_minutes == thread1_end_minutes and thread1_hours == thread1_end_hours and thread1_days == thread1_end_days and thread1_months == thread1_end_months and thread1_years == thread1_end_years:
                                    break
                                thread1_years -= 1
                                thread1_months = 12
       # print("Current")
        beep(sound='plink')
        print(date_str.format(thread1_years, thread1_months, thread1_days, thread1_hours, thread1_minutes, thread1_seconds))
        print("Countdown has ended!")


class Chrono(Thread):
    stop_chrono = False

    def stop(self):
        self.stop_chrono = True

    def run(self):
        thread_seconds = 0
        thread_seconds_follower = 0
        thread_minutes = 0
        thread_minutes_follower = 0
        thread_hours = 0
        thread_hours_follower = 0
        thread_days = 0
        thread_days_follower = 0
        thread_years = 0
        x = datetime.now()
        start_point = "\r\n"+"The start point is {}"
        print(start_point.format(x))
        while not self.stop_chrono:
            sleep(1)
            x += timedelta(seconds=1)
            thread_seconds += 1
            thread_seconds_follower += 1
            if thread_seconds_follower == 60:
                thread_minutes += 1
                thread_minutes_follower += 1
                thread_seconds_follower = 0
            else:
                if thread_minutes_follower == 60:
                    thread_hours += 1
                    thread_hours_follower += 1
                    thread_minutes_follower = 0
                else:
                    if thread_hours_follower == 24:
                        thread_days += 1
                        thread_days_follower += 1
                        thread_hours_follower = 0
                    else:
                        if thread_days_follower == 364:
                            thread_years += 1
                            thread_days_follower = 0
        elapsed_time_since_start = "\r\n"+"in {0} years in {1} days in {2} in hours {3} in minutes in {4} in seconds since start {5}"+"\r\n"
        sleep(0.100)
        beep(sound='plink')
        print(elapsed_time_since_start.format(thread_years, thread_days, thread_hours, thread_minutes, thread_seconds, x))


while another_device:
    sleep(0.100)
    stop_countdown = True
    try:
        choice = input("\r\n"+"What kind of device do you want to use?: 0:Chronometer 1:Countdown 2:None?")
        choice = int(choice)
        if choice == 0:
            thread = Chrono()
            chrono_threads.append(thread)
            thread.start()
        elif choice == 1:
            date_entry = input('Enter a start date for your countdown in YYYY-MM-DD-HH-mm-ss format:')
            year, month, day, hours, minutes, seconds = map(int, date_entry.split('-'))
           # print(year, month, day, hours, minutes, seconds)
            if month > 12 or day > 31 or hours > 23 or minutes > 59 or seconds > 59:
                print("Please add a valid value for month/day/hours/minutes/seconds")
                continue
            else:
                if month == 1 and day > 31:
                    print("January has only 31 days")
                    continue
                elif month == 2 and day > 28 :
                    print("February has only 28 days")
                    continue
                elif month == 3 and day > 31:
                    print("March has only 31 days")
                    continue
                elif month == 4 and day > 30:
                    print("April has only 30 days")
                    continue
                elif month == 5 and day > 31:
                    print("May has only 31 days")
                    continue
                elif month == 6 and day > 30 :
                    print("June has only 30  days")
                    continue
                elif month == 7 and day > 31:
                    print("July has only 31 days")
                    continue
                elif month == 8 and day > 31:
                    print("August has only 31 days")
                    continue
                elif month == 9 and day > 30:
                    print("September has only 30 days")
                    continue
                elif month == 10 and day > 31:
                    print("October has only 31 days")
                    continue
                elif month == 11 and day > 30:
                    print("November has only 30 days")
                    continue
                elif month == 12 and day > 31:
                    print("December has only 31 days")
                    continue
                else:
                    date_entry1 = input('Enter an end date for your countdown in YYYY-MM-DD-HH-mm-ss format:')
                    year1, month1, day1, hours1, minutes1, seconds1 = map(int, date_entry1.split('-'))
                 #   print(year1, month1, day1, hours1, minutes1, seconds1)
                    if month1 > 12 or day1 > 31 or hours1 > 23 or minutes1 > 59 or seconds1 > 59:
                        print("Please add a valid value for month/day/hours/minutes/seconds")
                        continue
                    else:
                        if month1 == 1 and day1 > 31:
                            print("January has only 31 days")
                            continue
                        elif month1 == 2 and day1 > 28:
                            print("February has only 28 days")
                            continue
                        elif month1 == 3 and day1 > 31:
                            print("March has only 31 days")
                            continue
                        elif month1 == 4 and day1 > 30:
                            print("April has only 30 days")
                            continue
                        elif month1 == 5 and day1 > 31:
                            print("May has only 31 days")
                            continue
                        elif month1 == 6 and day1 > 30:
                            print("June has only 30  days")
                            continue
                        elif month1 == 7 and day1 > 31:
                            print("July has only 31 days")
                            continue
                        elif month1 == 8 and day1 > 31:
                            print("August has only 31 days")
                            continue
                        elif month1 == 9 and day1 > 30:
                            print("September has only 30 days")
                            continue
                        elif month1 == 10 and day1 > 31:
                            print("October has only 31 days")
                            continue
                        elif month1 == 11 and day1 > 30:
                            print("November has only 30 days")
                            continue
                        elif month1 == 12 and day1 > 31:
                            print("December has only 31 days")
                            continue
                        else:
                            if year < year1 or month < month1 or day < day1 or hours < hours1 or minutes < minutes1 or seconds < seconds1:
                                print("Start Date must be in a later period than the end date in order to be a countdown")
                                continue
                            thread1 = Countdown()
                            countdown_threads.append(thread1)
                            thread1.start()
        elif choice == 2:
            choice = input("\r\n"+"Do you want to stop something? 0: Yes 1: No - (you exit the program) 2: I misstyped, take me back :)")
            choice = int(choice)
            if choice == 0:
                choice = input("\r\n"+"Choose 0: Chrono or 1: Countdown to shutdown")
                choice = int(choice)
                if choice == 0:
                    info_num_threads = "\r\n"+"You currently have {} Chronometer threads running:"+"\r\n"
                    print(info_num_threads.format(len(chrono_threads)))
                    print(chrono_threads)
                    choice = input("\r\n"+"Which Chronometer thread do you want to stop?")
                    choice = int(choice)
                    chrono_threads[choice].stop()
                    chrono_threads.pop(choice)
                    sleep(0.100)
                elif choice == 1:
                    info_num_threads = "\r\n"+"You currently have {} Countdown threads running:"+"\r\n"
                    print(info_num_threads.format(len(countdown_threads)))
                    print(countdown_threads)
                    choice = input("\r\n"+"Which Countdown thread do you want to stop?")
                    choice = int(choice)
                    countdown_threads[choice].stop()
                    countdown_threads.pop(choice)
                    sleep(0.100)
                else:
                    continue
            elif choice == 1:
                for x in chrono_threads:
                    a += 1
                    chrono_threads[a].stop()
                another_device = False
                for x in countdown_threads:
                    b += 1
                    countdown_threads[b].stop()
                    print("Exited program")
                another_device = False
                exit()
            elif choice == 2:
                continue
            else:
                print("Please choose only 0 or 1 or 2")
            continue
    except(ValueError, OverflowError, IndexError):
        print("Please add valid input.")