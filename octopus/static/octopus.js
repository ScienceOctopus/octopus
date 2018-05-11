$(document).ready(
    function () {
        $('#deflag').on( "click", function() {
            translate_to_german();
            $(this).preventDefault();
        });
    }
    );

function translate_to_german() {
    var translate = new AWS.Translate({'region': 'eu-west-1', 'accessKeyId': '', 'secretAccessKey': '', 'httpOptions': {'xhrAsync': false}});

    $('.translate').each(function(index) {
        var each_elem_text = $(this).text();
        var translated_text = '';

        var params = {
          SourceLanguageCode: 'en', /* required */
          TargetLanguageCode: 'de', /* required */
          Text: each_elem_text /* required */
        };
        translate.translateText(params, function (err, data) {
          if (err) console.log(err, err.stack); // an error occurred
          else     translated_text = data.TranslatedText;      // successful response
        });

        if (!!translated_text) {
            $(this).text(translated_text);
        }
    });
}