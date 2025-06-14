# Level AI Academy Brand Guidelines

## Brand Identity

### Mission Statement
Level AI Academy empowers individuals and organizations to master artificial intelligence through comprehensive, practical, and accessible education.

### Brand Values
- **Innovation**: Cutting-edge AI education
- **Accessibility**: Making AI learning available to everyone
- **Excellence**: High-quality, industry-relevant content
- **Community**: Collaborative learning environment

## Visual Identity

### Logo
- **Primary Logo**: "Level AI Academy" with modern, clean typography
- **Icon**: Stylized "LA" monogram with AI-inspired elements
- **Usage**: Always maintain clear space around logo (minimum 20px)

### Color Palette

#### Primary Colors
- **Primary Blue**: #2563EB (HSL: 217, 91%, 60%)
  - Use for primary actions, links, and brand emphasis
- **Deep Purple**: #7C3AED (HSL: 263, 76%, 58%)
  - Use for accents and highlights
- **Dark Gray**: #1F2937 (HSL: 215, 25%, 17%)
  - Use for primary text and headers

#### Secondary Colors
- **Teal Accent**: #14B8A6 (HSL: 174, 78%, 41%)
  - Use for success states and progress indicators
- **Orange Accent**: #F59E0B (HSL: 38, 92%, 50%)
  - Use for warnings and important notices
- **Light Gray**: #F3F4F6 (HSL: 210, 20%, 96%)
  - Use for backgrounds and cards

#### Gradient
- **Primary Gradient**: Linear gradient from Primary Blue to Deep Purple
  - Direction: 135deg
  - Use for hero sections and feature highlights

### Typography

#### Font Family
- **Headings**: Inter (font-weight: 600-800)
- **Body Text**: Inter (font-weight: 400-500)
- **Code/Technical**: JetBrains Mono or Fira Code

#### Font Sizes
- **H1**: 2.5rem (40px)
- **H2**: 2rem (32px)
- **H3**: 1.5rem (24px)
- **Body**: 1rem (16px)
- **Small**: 0.875rem (14px)

### Spacing & Layout
- **Base Unit**: 8px grid system
- **Container Max Width**: 1280px
- **Card Padding**: 24px
- **Section Spacing**: 48px-64px

## UI Components

### Buttons
- **Primary**: Background: Primary Blue, Text: White
- **Secondary**: Background: Light Gray, Text: Dark Gray
- **Border Radius**: 8px
- **Padding**: 12px 24px

### Cards
- **Background**: White
- **Border**: 1px solid #E5E7EB
- **Border Radius**: 12px
- **Shadow**: 0 1px 3px rgba(0, 0, 0, 0.1)

### Forms
- **Input Border**: #D1D5DB
- **Input Focus**: Primary Blue
- **Label Color**: Dark Gray
- **Helper Text**: #6B7280

## Content Guidelines

### Voice & Tone
- **Professional** yet approachable
- **Clear** and concise
- **Encouraging** and supportive
- **Technical** when necessary, but always accessible

### Course Categories
1. **Fundamentals of AI**
2. **Machine Learning**
3. **Deep Learning**
4. **Natural Language Processing**
5. **Computer Vision**
6. **AI Ethics & Responsibility**
7. **Practical AI Applications**
8. **AI for Business**

### Imagery
- Use modern, abstract representations of AI concepts
- Include diverse representations of learners
- Prefer illustrations over stock photos
- Maintain consistent visual style across all materials

## Implementation Notes

### CSS Variables
```css
:root {
  --color-primary: #2563EB;
  --color-secondary: #7C3AED;
  --color-accent-teal: #14B8A6;
  --color-accent-orange: #F59E0B;
  --color-text-primary: #1F2937;
  --color-text-secondary: #6B7280;
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F3F4F6;
  --gradient-primary: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
}
```

### Tailwind Config Extensions
- Extend theme with custom colors
- Add custom font families
- Configure spacing scale based on 8px grid