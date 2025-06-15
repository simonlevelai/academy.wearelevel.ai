# Level.ai Brand Guidelines for Academy

## Brand Identity

### Logo
- **Design**: Scales/friendly face design representing balance and accessibility
- **Usage**: Primary logo for headers, secondary simplified version for favicons
- **Colors**: Earthstone primary with Sunshine Yellow accents

### Color Palette

#### Primary Colors
- **Earthstone**: `#293f3b` - Primary text, headers, and navigation
- **Sunshine Yellow**: `#feda00` - Accent highlights and emphasis
- **Terra Green**: `#296b42` - Success states, progress indicators, completed items

#### Secondary Colors
- **Coral**: `#ff7f7a` - Buttons, CTAs, interactive elements (with Earthstone text)
- **Off-white**: `#fafafa` - Background and content areas
- **Light Grey**: `#f5f5f5` - Subtle backgrounds and dividers

### Typography

#### Primary Font Family
- **Body Text**: DM Sans (400, 500, 600, 700)
- **Headings**: Concert One (400) for major headings, DM Sans (600, 700) for subheadings
- **Code/Technical**: Source Code Pro for technical elements

#### Font Hierarchy
- **H1**: Concert One, 2.5rem, Earthstone
- **H2**: DM Sans 700, 2rem, Earthstone
- **H3**: DM Sans 600, 1.5rem, Earthstone
- **H4**: DM Sans 600, 1.25rem, Earthstone
- **Body**: DM Sans 400, 1rem, Earthstone
- **Caption**: DM Sans 400, 0.875rem, #666

## UI Components

### Buttons
- **Primary**: Coral background (#ff7f7a) with Earthstone text (#293f3b)
- **Secondary**: Earthstone outline with Earthstone text
- **Success**: Terra Green background with white text
- **Disabled**: Light grey background with grey text

### Cards and Containers
- **Background**: White with subtle shadow
- **Border**: Light grey (#e5e5e5)
- **Border Radius**: 8px for consistency
- **Padding**: 1.5rem standard

### Progress Indicators
- **Color**: Terra Green (#296b42)
- **Background**: Light grey (#f5f5f5)
- **Completion Badges**: Sunshine Yellow with Earthstone text

### Navigation
- **Background**: White with Earthstone text
- **Active States**: Sunshine Yellow background with Earthstone text
- **Hover States**: Light grey background

## Course Level Branding

### Level Color Coding
- **Level 1**: Sunshine Yellow (#feda00) - Foundations
- **Level 2**: Terra Green (#296b42) - User Competency
- **Level 3**: Coral (#ff7f7a) - Implementation Professional
- **Level 4**: Earthstone (#293f3b) - Strategic Leadership
- **Level 5**: Deep Terra (#1a4d2e) - Innovation & Advanced Practice

### Learning Path Visualization
- **Completed**: Terra Green with checkmark
- **Current**: Coral with progress indicator
- **Locked**: Light grey with lock icon
- **Available**: Sunshine Yellow with forward arrow

## Accessibility Requirements

### Color Contrast
- All text must meet WCAG 2.1 AA standards (4.5:1 minimum)
- Interactive elements must have 3:1 minimum contrast
- Focus indicators must be clearly visible

### Typography
- Minimum font size: 16px for body text
- Line height: 1.6 for readability
- Letter spacing: Optimized for dyslexia-friendly reading

### Interactive Elements
- All buttons minimum 44px touch target
- Clear hover and focus states
- Keyboard navigation support
- Screen reader friendly markup

## Voice and Tone

### Personality
- **Approachable**: Friendly but professional
- **Empowering**: Confidence-building language
- **Practical**: Focus on real-world application
- **Inclusive**: Welcoming to all skill levels

### Language Guidelines
- Use "you" and active voice
- Avoid jargon without explanation
- Include examples from charity sector
- Celebrate progress and achievements
- Address concerns with empathy

## Implementation Notes

### CSS Custom Properties
```css
:root {
  --color-earthstone: #293f3b;
  --color-sunshine: #feda00;
  --color-terra: #296b42;
  --color-coral: #ff7f7a;
  --color-background: #fafafa;
  --color-surface: #ffffff;
  --color-border: #e5e5e5;
  
  --font-body: 'DM Sans', sans-serif;
  --font-heading: 'Concert One', cursive;
  --font-code: 'Source Code Pro', monospace;
  
  --border-radius: 8px;
  --shadow-subtle: 0 1px 3px rgba(0,0,0,0.1);
  --spacing-unit: 1.5rem;
}
```

### Responsive Breakpoints
- **Mobile**: 320px - 768px
- **Tablet**: 768px - 1024px
- **Desktop**: 1024px+

### Animation Guidelines
- **Duration**: 200ms for micro-interactions, 300ms for page transitions
- **Easing**: ease-out for entering, ease-in for exiting
- **Respect**: prefers-reduced-motion for accessibility