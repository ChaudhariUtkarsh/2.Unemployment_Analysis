from pathlib import Path

# README file path
readme_path = Path("README.md")

if not readme_path.exists():
    print("ERROR: README.md file not found!")
else:
    content = readme_path.read_text(encoding="utf-8").lower()

    sections = {
        "Project Overview": ["project overview", "overview"],
        "Objectives": ["objectives", "objective"],
        "Kaggle Dataset Information": ["kaggle", "dataset"],
        "Technologies Used": ["technologies used", "tech stack"],
        "Project Features": ["project features", "features"],
        "Streamlit Dashboard Features": ["streamlit dashboard", "dashboard features"],
        "Project Structure": ["project structure"],
        "Installation and Setup": ["installation", "setup"],
        "Requirements": ["requirements"],
        "Limitations": ["limitations"],
        "Conclusion": ["conclusion"]
    }

    print("\nREADME.md VERIFICATION")
    print("=" * 50)

    passed = 0
    missing = []

    for section, keywords in sections.items():
        found = any(keyword in content for keyword in keywords)

        if found:
            print(f"[PASS] {section}")
            passed += 1
        else:
            print(f"[MISSING] {section}")
            missing.append(section)

    print("\n" + "=" * 50)
    print(f"Total Sections: {len(sections)}")
    print(f"Available Sections: {passed}")
    print(f"Missing Sections: {len(missing)}")

    if not missing:
        print("\nSUCCESS: README.md Verification Completed!")
    else:
        print("\nPlease update these sections:")
        for section in missing:
            print("-", section)