// // function calculateMedia(twoMonths1, twoMonths2, weightSemesterOne, weightSemesterTwo) {
// //   return ((twoMonths1 * weightSemesterOne) + (twoMonths2 * weightSemesterTwo)) / (weightSemesterOne + weightSemesterTwo);
// // }

// // function createParagraph(content) {
// //   const paragraph = document.createElement('p');
// //   paragraph.innerHTML = content;
// //   return paragraph;
// // }

// // function updateResult(resultElement, value) {
// //   resultElement.value = value;
// // }

// // function removeExistingParagraph(containerElement) {
// //   const existingParagraph = containerElement.querySelector('p');
// //   if (existingParagraph) {
// //       existingParagraph.remove();
// //   }
// // }

// // function displayResultMessage(formSemester, result, valueRequired) {
// //   const paragraph = createParagraph(result >= valueRequired ? 'Você atingiu a nota necessária' : `Você precisa de ${result.toFixed(2)} para atingir a média`);
// //   formSemester.appendChild(paragraph);
// // }

function calcAverageSemester() {
    const monthOne = parseFloat(document.querySelector('#month-1').value) || 0;
    const monthTwo = parseFloat(document.querySelector('#month-2').value) || 0;
    const monthTree = parseFloat(document.querySelector('#month-3').value) || 0;
    const monthFour = parseFloat(document.querySelector('#month-4').value) || 0;


    const weightSemesterOne = 2;
    const weightSemesterTwo = 3;

    const result1 = document.querySelector('#result1');
    const valueRequired = 60;

    const formSemester = document.querySelector('#form-semester');

    const media = calculateMedia(monthOne, monthTwo, monthTree, monthFour, weightSemesterOne, weightSemesterTwo);
    updateResult(result1, media);

    removeExistingParagraph(formSemester);

    const result = valueRequired - media;
    console.log(result)
    displayResultMessage(formSemester, result, valueRequired);
}

document.querySelector('#calc-average-semester').addEventListener("click", calcAverageSemester);
