
// To grab API KEYS from .env file
require('dotenv').config()

//  Start Twit with KEYS from process.env
var Twit = require('twit')
var T = new Twit({
    consumer_key: process.env.consumer_key,
    consumer_secret: process.env.consumer_secret,
    access_token: process.env.access_token,
    access_token_secret: process.env.access_token_secret,
})

// Read data into array of objects
var loader = require('csv-load-sync');
var csv_data = loader('/Users/geoffreyhughes/Projects/Covid19_bot/data/state_NYT_clean.csv');

csv_data.forEach(state => console.log(state.date, ' ', state.state, ' has ', state.cases, ' cases and ', state.deaths, ' dead.',
'#'.concat( state.state.replace(/\s/g, ''))));

// Reformat date to mm-dd-yyyy
var date_today = csv_data[0].date
var date_today_array = date_today.split('-')
date_today = date_today_array[1].concat('/', date_today_array[2], '/', date_today_array[0])
console.log(date_today)

// Head tweet, begins daily thread
T.post('statuses/update', { status: '[' + date_today +
"]: United States COVID-19 statistics by State. Data is cumulative and provided by @nytimes. Daily thread (alphabetical) #COVID19" }, function(err, data, response) {
  console.log(data)
  reply_tweet(data.id_str, 0)
})

// As needed
//reply_tweet(1310106912785006594, ... )

// Recursive reply chain thread
function reply_tweet(parent_id, curr_state) {

  var loader = require('csv-load-sync');
  var csv_data = loader('/Users/geoffreyhughes/Projects/Covid19_bot/data/state_NYT_clean.csv');

  console.log(parent_id);
  T.post('statuses/update', {in_reply_to_status_id: parent_id, auto_populate_reply_metadata: true,
    status: '(' + csv_data[curr_state].state + '): ' + csv_data[curr_state].cases +
    ' cases and ' + csv_data[curr_state].deaths + ' deaths. ' + '#'.concat( csv_data[curr_state].state.replace(/\s/g, '')) +
    ' @Covid19States'}, function(err, data, response) {

      // Rows of list (states / territtories))
      if (curr_state < 5) {
        curr_state += 1;
        reply_tweet(data.id_str, curr_state)
      }
    })


}
