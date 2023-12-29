function calculateMedia(twoMonths1, twoMonths2, weightSemesterOne, weightSemesterTwo) {
  return ((twoMonths1 * weightSemesterOne) + (twoMonths2 * weightSemesterTwo)) / (weightSemesterOne + weightSemesterTwo);
}

function createParagraph(content) {
  const paragraph = document.createElement('p');
  paragraph.id = "note"
  paragraph.innerHTML = content;
  return paragraph;
}

function updateResult(resultElement, value) {
  resultElement.value = value;
}

function removeExistingParagraph(containerElement) {
 const existingParagraph = containerElement.querySelector('#note');
 if (existingParagraph) {
     existingParagraph.remove();
 }
}

function displayResultMessage(formSemester, result, valueRequired, media) {
  const paragraph = createParagraph(media >= valueRequired ? 'Você atingiu a nota necessária' : `Você precisa de ${result.toFixed(2)} para atingir a média`);
  formSemester.appendChild(paragraph);
}

function calcAverageSemester() {
  const twoMonths1 = parseFloat(document.querySelector('#two-months-1').value) || 0;
  const twoMonths2 = parseFloat(document.querySelector('#two-months-2').value) || 0;

  const weightSemesterOne = 2;
  const weightSemesterTwo = 3;

  const result1 = document.querySelector('#result1');
  const valueRequired = 60;

  const formSemester = document.querySelector('#form-semester');

  const media = calculateMedia(twoMonths1, twoMonths2, weightSemesterOne, weightSemesterTwo);
  updateResult(result1, media);

  removeExistingParagraph(formSemester);

  const result = (valueRequired * (weightSemesterOne + weightSemesterTwo)) - (media * (weightSemesterOne + weightSemesterTwo));
  displayResultMessage(formSemester, result, valueRequired, media);
}

document.querySelector('#calc-average-semester').addEventListener("click", calcAverageSemester);

// Media anual
 
function calculateMediaAnnual(monthOne, monthTwo, monthTree, monthFour, weightSemesterOne, weightSemesterTwo) {
  return ((monthOne * weightSemesterOne) + (monthTwo * weightSemesterOne) + (monthTree * weightSemesterTwo) + (monthFour * weightSemesterTwo)) / (weightSemesterOne * 2 + weightSemesterTwo * 2);
}

function createParagraphMediaAnnual(content) {
  const paragraph = document.createElement('p');
  paragraph.id = "note"
  paragraph.innerHTML = content;
  return paragraph;
}

function updateResultMediaAnnual(resultElement, value) {
  resultElement.value = value;
}

function removeExistingParagraphMediaAnnual(containerElement) {
  const existingParagraph = containerElement.querySelector('#note');
  if (existingParagraph) {
      existingParagraph.remove();
  }
}

function displayResultMessageMediaAnnual(formSemester, result, valueRequired, media) {
  const paragraph = createParagraphMediaAnnual(media >= valueRequired ? 'Você atingiu a nota necessária' : `Você precisa de ${result.toFixed(2)} para atingir a média`);
  formSemester.appendChild(paragraph);
}

function calcAverageAnnual() {
  const monthOne = parseFloat(document.querySelector('#month-1').value) || 0;
  const monthTwo = parseFloat(document.querySelector('#month-2').value) || 0;
  const monthTree = parseFloat(document.querySelector('#month-3').value) || 0;
  const monthFour = parseFloat(document.querySelector('#month-4').value) || 0;

  const weightSemesterOne = 2;
  const weightSemesterTwo = 3;

  const resultAnnual = document.querySelector('#result-annual');
  const valueRequired = 60;

  const formAnnual = document.querySelector('#form-annual');

  // Considerar peso 3 nas notas que faltam
  const media = calculateMediaAnnual(monthOne, monthTwo, monthTree, monthFour, weightSemesterOne, weightSemesterTwo);
  updateResultMediaAnnual(resultAnnual, media);

  removeExistingParagraphMediaAnnual(formAnnual);

  // Considerar peso 3 nas notas que faltam
  const result = (valueRequired * (weightSemesterOne * 2 + weightSemesterTwo * 2)) - (media * (weightSemesterOne * 2 + weightSemesterTwo * 2));
  displayResultMessageMediaAnnual(formAnnual, result, valueRequired, media);
}

document.querySelector('#calc-average-annual').addEventListener("click", calcAverageAnnual);
