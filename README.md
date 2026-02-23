# Python Memory & Data Types Study

- **Reference-Based Assignment:** Learned that Python variables are just labels (references) pointing to objects in the heap.
- **Memory Visualization:** Visualized how `x = 10` creates an object at a memory address (e.g., `0x1001`) while `x` acts as the pointer.
- **Immutability (Integers/Strings):** Reassigning `y = 11` doesn't change `x`; it creates a brand new object because these types can't be modified in place.
- **Mutability (Lists):** Demonstrated that `y = x` shares a reference, meaning modifying `y` directly affects `x` unless a copy is made.
- **Cloning Techniques:** Practiced the difference between **assignment** (reference) vs. **slicing** (`[:]`) and `.copy()` to safely duplicate data.
