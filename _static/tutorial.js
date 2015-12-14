$(document).ready(function() {
  var $articleBody = $('div[itemprop=articleBody]')

  $articleBody.on('click', '.exercise-hint button', function() {
    $(this).next('div').toggleClass('hidden')
    $(this).parent('.exercise-hint').toggleClass('shown')
  })

  $articleBody.find('.hintlist').each(function() {
    $(this).toggleClass('hidden')
    $(this).find('ol li').each(function() {
      var li = $(this)
      var newSpan = $('<span class="hidden"></span>')
      newSpan.append(li.contents())
      var button = $('<button>Show hint</button>')
      button.on('click', function() {
        newSpan.toggleClass('hidden')
      })
      li.append(button)
      li.append(newSpan)
    })
  })

  $articleBody.fitVids()
});
