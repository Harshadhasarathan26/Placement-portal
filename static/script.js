// Add simple entrance animations for glass cards and interactivity
document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll('.glass-card');
    
    // Animate cards sequentially to create a cascading entrance effect
    cards.forEach((card, index) => {
        card.animate([
            { opacity: 0, transform: 'translateY(30px)' },
            { opacity: 1, transform: 'translateY(0)' }
        ], {
            duration: 600,
            delay: index * 80, // Adjust delay multiplier for staggered effect
            fill: 'both',
            easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
        });
    });

    // Auto-dismiss Flash Messages after 5 seconds if present
    const flashMessages = document.querySelectorAll('.flash-msg');
    if(flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.animate([
                    { opacity: 1, transform: 'translateY(0)' },
                    { opacity: 0, transform: 'translateY(-10px)' }
                ], {
                    duration: 400,
                    fill: 'both',
                    easing: 'ease-in'
                });
                // Remove from DOM after animation
                setTimeout(() => msg.remove(), 400);
            });
        }, 5000); // 5000ms = 5 seconds
    }
});

// Progress Tracking for Role Roadmaps
function toggleProgress(roleId, step, isCompleted) {
    const textSpan = document.getElementById(`step-text-${step}`);
    if (isCompleted) {
        textSpan.style.textDecoration = 'line-through';
        textSpan.style.opacity = '0.7';
    } else {
        textSpan.style.textDecoration = 'none';
        textSpan.style.opacity = '1';
    }

    fetch('/api/progress', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            role_id: roleId,
            step: parseInt(step),
            is_completed: isCompleted
        })
    }).catch(err => console.error('Error saving progress:', err));
}

// Mock Interview Evaluation Stub
function evaluateAnswer() {
    const answer = document.getElementById('mock_answer').value;
    if (!answer.trim()) {
        alert("Please enter a response first.");
        return;
    }
    
    document.getElementById('eval-loading').style.display = 'inline-block';
    document.getElementById('eval-result').style.display = 'none';
    
    // Simulate AI API delay
    setTimeout(() => {
        document.getElementById('eval-loading').style.display = 'none';
        const resultDiv = document.getElementById('eval-result');
        
        // Very basic mock heuristic logic for demonstration 
        let score = 50;
        let feedback = "A decent start, but your answer lacks depth.";
        
        if (answer.length > 50) {
            score += 20;
            feedback = "Good detail. Try focusing on the STAR method (Situation, Task, Action, Result) to format it better.";
        }
        if (answer.toLowerCase().includes("example") || answer.toLowerCase().includes("result")) {
            score += 15;
            feedback = "Excellent use of specific examples to back up your point!";
        }
        
        document.getElementById('result-score').innerText = `${score}/100`;
        // update color based on heuristic
        document.getElementById('result-score').style.color = score > 70 ? '#16a34a' : '#ea580c';
        
        // Show result
        resultDiv.style.display = 'block';
    }, 1500);
}
