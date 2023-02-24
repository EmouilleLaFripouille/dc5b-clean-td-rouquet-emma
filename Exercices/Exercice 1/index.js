const fs = require('fs');
const csvParser = require('csv-parser');
var counter = 0;

fs.createReadStream('/Users/emmarouquet/DC5B/dc5b-clean-td-rouquet-emma/Exercices/Exercice 1/electronic-card-transactions-december-2022-csv-tables.csv')
 .pipe(csvParser())
 .on('data', (data) => {
   if (counter < 20){
      console.log(data);
   }
    counter++;
 })
 .on('end', () => {
    console.log('Affichage terminée');
 });
