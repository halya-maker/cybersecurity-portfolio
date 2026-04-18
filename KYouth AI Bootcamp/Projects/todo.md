# RakanBank - Rakan AI Inclusive Banking Assistant - TODO

## Core Features

### Phase 1: Project Structure
- [x] Initialize project structure and dependencies
- [x] Create todo.md with feature tracking

### Phase 2: Core Layout & Accessibility Toolbar
- [x] Build Header component with persistent accessibility toolbar
- [x] Implement High Contrast toggle (WCAG AAA support)
- [x] Implement Text Size adjuster (3 levels: small, medium, large)
- [x] Implement Language toggle (Bahasa Malaysia / English)
- [x] Implement Read Aloud button with text-to-speech
- [x] Implement Voice Navigation toggle with SpeechRecognition API
- [x] Build Hero section with Rakan AI greeting avatar
- [x] Build Action Grid with 4 large tiles (Send Money, Pay Bills, Recent Activity, My Savings)
- [x] Build Sticky Bottom Navigation Footer with large tap targets
- [x] Ensure all components have ARIA landmarks and semantic HTML

### Phase 3: Accessibility Features
- [x] Add ARIA labels to all interactive elements
- [x] Implement visible focus rings (keyboard navigation)
- [x] Ensure 4.5:1 minimum contrast ratio across all text
- [x] Add screen-reader-friendly descriptions
- [x] Test keyboard navigation (Tab, Enter, Escape)
- [x] Implement focus management in modals and flows
- [x] Add skip-to-content link

### Phase 4: Focus Mode Flows
- [x] Build Send Money flow:
  - [x] Screen 1: Recipient selection (contact grid + new person button)
  - [x] Screen 2: Amount entry (large keypad with audio readout)
  - [x] Screen 3: Confirmation screen with swipe/hold-to-confirm
  - [x] Success feedback (chime + animation)
- [x] Build Pay Bills flow:
  - [x] Screen 1: Biller selection (large logos)
  - [x] Screen 2: Amount entry (auto-fill if scanned, large keypad)
  - [x] Screen 3: Confirmation & receipt
  - [x] Success feedback (chime + animation)
- [x] Build Recent Activity screen:
  - [x] Transaction list as large vertical cards
  - [x] Color-coded amounts (green in, black/red out)
  - [x] Audio playback for each transaction
  - [x] Simple language formatting
- [x] Build My Savings screen:
  - [x] Display savings balance in large typography
  - [x] Visual progress bar toward goal
  - [x] Add Money and Take Money Out buttons

### Phase 5: Rakan AI Chat Assistant
- [x] Integrate LLM for conversational banking queries
- [x] Build floating chat button
- [x] Implement chat interface with message history
- [x] Add multi-language support (BM/English)
- [x] Implement Jargon Translator for banking terms
- [x] Add streaming support for LLM responses
- [x] Ensure chat is accessible via keyboard and screen readers

### Phase 6: Success Feedback & Polish
- [x] Add success chime sound effect
- [x] Add success animation (visual feedback)
- [x] Implement device vibration feedback
- [x] Add loading states for all async operations
- [x] Implement error handling with clear messaging
- [x] Add empty states for transaction lists
- [x] Test WCAG 2.1 AA compliance across all pages
- [x] Add animations for Focus Mode transitions
- [x] Optimize for mobile and tablet devices

### Phase 7: Testing & Delivery
- [x] Write vitest tests for accessibility features
- [x] Write vitest tests for banking flows
- [x] Write vitest tests for LLM integration
- [x] Manual accessibility testing with screen readers (NVDA/VoiceOver)
- [x] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [x] Mobile device testing
- [x] Create checkpoint and deliver to user

## Implementation Notes

- All text must be available in Bahasa Malaysia and English
- Minimum button size: 44x44 pixels (WCAG 2.5.5)
- Minimum contrast ratio: 4.5:1 for normal text, 3:1 for large text (WCAG 1.4.6)
- All flows must be non-scrollable single-layer dashboard strategy
- Voice commands for hands-free navigation
- Simplified language for banking terminology
- Multi-sensory feedback (audio + visual + haptic)

### Phase 8: Additional Features
- [x] Add SOS - Get Help Now button with emergency contacts popup
- [x] Replace Rakan AI chatbot with Jotform agent embed
- [x] Add HeyGen video player above Send Money flow
- [x] Test SOS button functionality
- [x] Test Jotform agent integration
- [x] Test video player autoplay and muting

### Phase 9: Transaction History Feature
- [x] Create Transaction History page with advanced filtering
- [x] Implement date range filter (from/to dates)
- [x] Implement transaction type filter (All, Sent, Received, Bills Paid)
- [x] Add sorting options (newest first, oldest first, amount high-to-low, amount low-to-high)
- [x] Create transaction detail view modal
- [x] Add export/download transaction history option
- [x] Implement search by recipient/biller name
- [x] Add transaction statistics (total sent, total received, total bills paid)
- [x] Ensure Transaction History is accessible and responsive
- [x] Add Transaction History to navigation menu
- [x] Write vitest tests for Transaction History filtering
- [x] Test Transaction History with screen readers

### Phase 10: Recurring Bills & Scheduled Transfers Notifications
- [x] Create recurring bills and scheduled transfers data types
- [x] Create mock data for recurring bills and scheduled transfers
- [x] Build Notifications Center page with upcoming reminders
- [x] Implement notification banner on home page
- [x] Create notification alert component with dismissal
- [x] Add browser notifications API integration
- [x] Implement notification preferences (enable/disable, notification timing)
- [x] Add sound alerts for upcoming bills
- [ ] Create recurring bill management UI (add, edit, delete recurring bills)
- [ ] Add scheduled transfer management UI
- [x] Implement notification scheduling logic
- [x] Add i18n translations for notifications
- [x] Ensure notifications are accessible (ARIA labels, screen reader support)
- [x] Test notifications with various screen sizes

### Phase 11: UI Cleanup
- [x] Remove Send Money, Pay Bills, Activity, and Savings from sticky footer
- [x] Keep only Home and History buttons in footer
- [x] Ensure Action Grid buttons are the primary navigation
- [x] Position SOS emergency button on top of chatbot (z-index adjustment)
- [x] Remove HeyGen video from Send Money flow
- [x] Remove HeyGen video from Pay Bills flow
- [x] Add user-uploaded BankSafety.mp4 video to home page below hero section
- [x] Configure video with autoplay, muted, and controls
