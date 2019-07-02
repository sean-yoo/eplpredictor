var tabulate = function (data,columns) {
    var table = d3.select('body').append('table')
      var thead = table.append('thead')
      var tbody = table.append('tbody')
  
      thead.append('tr')
        .selectAll('th')
          .data(columns)
          .enter()
        .append('th')
          .text(function (d) { return d })
  
      var rows = tbody.selectAll('tr')
          .data(data)
          .enter()
        .append('tr')
  
      var cells = rows.selectAll('td')
          .data(function(row) {
              return columns.map(function (column) {
                  return { column: column, value: row[column] }
            })
        })
        .enter()
      .append('td')
        .text(function (d) { return d.value })
  
    return table;
  }
  
d3.csv('/data/standings/2013.csv',function (data) {
    var columns = ['Team', 'GamesPlayed', 'Points', 'GoalsFor', 'GoalsAgainst', 'GoalDifference', 'Shots', 'ShotsPerGame']
    tabulate(data,columns)
})