document.addEventListener("DOMContentLoaded", function() {
    let cropName = localStorage.getItem("cropName") || "Unknown Crop";
    let totalExpenses = parseFloat(localStorage.getItem("totalExpenses")) || 0;

    document.getElementById("cropInfo").innerHTML = `Crop: <b>${cropName}</b>`;
    document.getElementById("expenseDisplay").innerText = `₹${totalExpenses}`;
});

function calculateProfitLoss() {
    let totalExpenses = parseFloat(localStorage.getItem("totalExpenses")) || 0;
    let salePrice = parseFloat(document.getElementById("salePrice").value) || 0;
    let profitLossAmount = salePrice - totalExpenses;

    let resultElement = document.getElementById("profitLossResult");
    let suggestionElement = document.getElementById("suggestions");

    if (profitLossAmount > 0) {
        resultElement.innerHTML =  `<span style="color:green; font-weight:bold;">Profit: ₹${profitLossAmount.toFixed(2)}</span>`;
        suggestionElement.innerHTML = `<h3>💡 Tips to Increase Profit:</h3>
            <ul>
                <li>Use high-quality seeds for better yield.</li>
                <li>Optimize fertilizer usage to reduce costs.</li>
                <li>Sell crops at better market rates.</li>
                <li>Reduce storage and transportation costs.</li>
            </ul>`;
    } else if (profitLossAmount < 0) {
        let lossAmount = Math.abs(profitLossAmount);
        resultElement.innerHTML =  <span style="color:red; font-weight:bold;">Loss: ₹${lossAmount.toFixed(2)}</span>;
        suggestionElement.innerHTML = `<h3>🚨 How to Reduce Loss:</h3>
            <ul>
                <li>Reduce labour costs by using machinery.</li>
                <li>Apply fertilizers efficiently to avoid overuse.</li>
                <li>Find better market prices before selling.</li>
                <li>Minimize unnecessary expenses in land preparation and harvesting.</li>
            </ul>`;
    } else {
        resultElement.innerHTML = `⚖ No Profit, No Loss.`;
        suggestionElement.innerHTML = "";
    }
}

let totalExpense = 0;
import totalExpenses from "./expence.js";

document.getElementById("calc").addEventListener("click", () => {
    let profitLoss = parseFloat(document.getElementById("calc").value)
    console.log(totalExpenses)
    let ans = document.getElementsByClassName("ans")[0]
    if(profitLoss >= totalExpenses){
        ans.innerHTML = `You are in profit of ${profitLoss - totalExpenses}`
    }
    else {
        ans.innerHTML = `You are in loss of ${totalExpenses - profitLoss}`
    }
})