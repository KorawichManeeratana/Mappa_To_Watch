const jsonData = "app.json"
    var titleElement = document.getElementById("title");

    document.getElementById("action").addEventListener("click", function(event) {
        event.preventDefault();

        var selectedName = event.target.getAttribute("name");
    

    function updateContent(selectedName) {
        const content = jsonData.find(item => item.name === selectedName);
        if (content) {
          // Update the title
          document.getElementById("title").textContent = content.name;
      
          // Update the introduction
          document.getElementById("introduction").textContent = content.introduction;
      
          // Update the genre
          document.getElementById("gen").textContent = content.genre;
        } else {
          // Handle if the selected item is not found in the JSON data
          alert("Content not found");
        }
      }

      document.getElementById("rest_card").addEventListener("click", function() {
        updateContent(selectedName);
      })
});
