# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a React-based recipe sharing frontend application created with Create React App. Currently implements a landing page with email waitlist functionality.

## Development Commands

### Core Commands
- `npm start` - Start development server (http://localhost:3000)
- `npm test` - Run tests in interactive watch mode
- `npm run build` - Build for production
- `npm run eject` - Eject from Create React App (one-way operation)

### Testing
- Tests use Jest and React Testing Library
- Test files follow the pattern `*.test.js`
- Run `npm test` for interactive test runner

## Architecture

### Project Structure
- `src/App.js` - Main application component with waitlist functionality
- `src/index.js` - React app entry point
- `src/App.css` - Main application styles
- `public/` - Static assets and HTML template
- Standard Create React App structure

### Key Components
- **App Component**: Main landing page with email collection form
- **State Management**: Uses React useState hooks for form state
- **Styling**: CSS-in-JS approach with external stylesheets

### Technology Stack
- React 19.1.1
- Create React App 5.0.1
- React Testing Library for testing
- Standard ESLint configuration (react-app preset)

## Current Functionality
The application currently features:
- Landing page for recipe sharing platform
- Email waitlist signup form
- Success state after email submission
- Responsive design considerations