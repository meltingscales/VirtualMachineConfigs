// https://www.codewars.com/kata/extended-weekends

print = console.log

const SUNDAY = 0;
const MONDAY = 1;
const TUESDAY = 2;
const WEDNESDAY = 3;
const THURSDAY = 4;
const FRIDAY = 5;
const SATURDAY = 6;

const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"];

/**
 * Tells you how many days of a specific type there are in a month.
 *
 * Example: count_days(2018, 11, SATURDAY) -> 5
 */
function count_days(year, month, whichday) {

    var day, counter, date;

    day = 1;
    counter = 0;
    date = new Date(year, month, day);
    
    while (date.getMonth() === month) {
    
        if (date.getDay() === whichday) { // Sun=0, Mon=1, Tue=2, etc.
            counter += 1;
        }
        
        day += 1;
        date = new Date(year, month, day);
    }
    return counter;
}


/**
 * Tells you if a date's month is an 'extended weekend', which means
 * that it has 5 Fridays, Saturdays, and Sundays.
 */
function isExtendedWeekend(year, month) {
  if ((count_days(year, month, SATURDAY) >= 5) &&
     (count_days(year, month, SUNDAY) >= 5) &&
     (count_days(year, month, FRIDAY) >= 5)) {
    return true;
  }
  return false;
}

function solve(a, b) {

    var last_month, first_month;
    var total_months = 0;

    // For all years,
    for(var year = a; year <= b; year++) {
    
      // For all months (0 to 11),
      for(var month = 0; month <= 11; month++) {
          
          // If it has 5 Fridays, Saturdays, and Sundays,
          if(isExtendedWeekend(year, month)) {

            // We've found one more month!
            total_months++;
            
            // The first month we check.
            if(first_month === undefined) { 
              first_month = month;
            }

            // The last month we check.
            last_month = month;
            
            
            //print(`${month} ${year} has an extended weekend.`)
          }
          
      }
    }
    
    return [
      monthNames[first_month].slice(0, 3), // The first month name
      monthNames[last_month].slice(0, 3),
      total_months]
}