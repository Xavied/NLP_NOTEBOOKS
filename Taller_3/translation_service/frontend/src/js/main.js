// Global variables for source and target languages (default: English to Spanish)
let sourceLang = "en";
let targetLang = "es";

const sourceTabs = document.querySelectorAll("#sourceTabs .tab-btn");
const targetTabs = document.querySelectorAll("#targetTabs .tab-btn");

// Text areas and display
const inputText = document.getElementById("inputText");
const translatedTextDiv = document.getElementById("translatedText");
const translateBtn = document.getElementById("translateBtn");
const charCount = document.getElementById("charCount");

// Swap button
const swapBtn = document.getElementById("swapBtn");

// Update character count as user types (max 255 characters)
inputText.addEventListener("input", () => {
  charCount.textContent = `${inputText.value.length}/255`;
});

// Function to handle active state on tab click
function activateTab(tabs, selectedTab) {
  tabs.forEach(tab => tab.classList.remove("active"));
  selectedTab.classList.add("active");
}

// Function to update target tabs availability based on sourceLang
function updateTargetTabsAvailability() {
  targetTabs.forEach(tab => {
    if (tab.getAttribute("data-lang") === sourceLang) {
      // Disable this target option
      tab.classList.add("disabled");
      tab.disabled = true;
      // If this is currently selected, switch to a different tab
      if (targetLang === sourceLang) {
        for (const otherTab of targetTabs) {
          if (otherTab.getAttribute("data-lang") !== sourceLang) {
            targetLang = otherTab.getAttribute("data-lang");
            activateTab(targetTabs, otherTab);
            break;
          }
        }
      }
    } else {
      tab.classList.remove("disabled");
      tab.disabled = false;
    }
  });
}

// Source tabs event listener
sourceTabs.forEach(tab => {
  tab.addEventListener("click", () => {
    activateTab(sourceTabs, tab);
    sourceLang = tab.getAttribute("data-lang");
    updateTargetTabsAvailability();
  });
});

// Target tabs event listener
targetTabs.forEach(tab => {
  tab.addEventListener("click", () => {
    // Only allow selection if not disabled
    if (!tab.disabled) {
      activateTab(targetTabs, tab);
      targetLang = tab.getAttribute("data-lang");
    }
  });
});

// Swap button event
swapBtn.addEventListener("click", () => {
  // Swap language variables
  [sourceLang, targetLang] = [targetLang, sourceLang];

  // Update source tabs
  sourceTabs.forEach(tab => {
    if (tab.getAttribute("data-lang") === sourceLang) {
      activateTab(sourceTabs, tab);
    }
  });
  // Update target tabs
  targetTabs.forEach(tab => {
    if (tab.getAttribute("data-lang") === targetLang) {
      activateTab(targetTabs, tab);
    }
  });

  updateTargetTabsAvailability();
  
  // Move the translated text into the input box
  const currentTranslation = translatedTextDiv.textContent.trim();
  if (currentTranslation !== "") {
    inputText.value = currentTranslation;
    charCount.textContent = `${inputText.value.length}/255`;
    translatedTextDiv.textContent = "";
  }
});

// Translate button event
translateBtn.addEventListener("click", async () => {
  const text = inputText.value.trim();
  if (text.length === 0) {
    alert("Por favor, ingresa un texto para traducir.");
    return;
  }
  if (text.length > 255) {
    alert("El texto a traducir no puede exceder los 255 caracteres.");
    return;
  }
  
  const payload = {
    text: text,
    source: sourceLang,
    target: targetLang,
  };

  try {
    const response = await fetch("http://localhost:5555/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    
    if (response.ok) {
      translatedTextDiv.textContent = data.translated_text;
    } else {
      translatedTextDiv.textContent = `Error: ${data.error}`;
    }
  } catch (error) {
    translatedTextDiv.textContent = `Request failed: ${error.message}`;
  }
});
