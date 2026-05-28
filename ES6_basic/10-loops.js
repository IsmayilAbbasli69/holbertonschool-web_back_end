export default function appendToEachArrayValue(array, appendString) {
  const final = [];
  for (const value of array) {
    final.push(appendString + value);
  }

  return final;
}
