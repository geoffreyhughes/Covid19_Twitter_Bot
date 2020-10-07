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

// Get MM/DD/YYYY for tweeting purposes
var dateObj = new Date();
var month = dateObj.getUTCMonth() + 1; //months from 1-12
var day = dateObj.getUTCDate();
var year = dateObj.getUTCFullYear();

curr_date = month + "/" + day + "/" + year;

//
// post a tweet with media
//
const fs = require('fs');
var b64content = fs.readFileSync('/Users/geoffreyhughes/Projects/Covid19_Twitter_Bot/data/live/graphs/most_recent_bar_graph.png',
 { encoding: 'base64' })

// first we must post the media to Twitter
T.post('media/upload', { media_data: b64content }, function (err, data, response) {
  // now we can assign alt text to the media, for use by screen readers and
  // other text-based presentations and interpreters
  var mediaIdStr = data.media_id_string
  var altText = "Cumulative COVID-19 Cases and Deaths in the United States"
  var meta_params = { media_id: mediaIdStr, alt_text: { text: altText } }

  T.post('media/metadata/create', meta_params, function (err, data, response) {
    if (!err) {
      // now we can reference the media and post a tweet (media will attach to the tweet)
      var params = { status: '[' + curr_date + ']: Cumulative COVID-19 Cases and Deaths in the United States', media_ids: [mediaIdStr] }

      T.post('statuses/update', params, function (err, data, response) {
        console.log(data)
      })
    }
  })
})
