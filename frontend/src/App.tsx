import { AutoApplyButton } from './components/AutoApplyButton';

export const App = () => {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      <h1 style={{ marginBottom: '40px', color: '#333' }}>Auto Apply</h1>
      <AutoApplyButton />
    </div>
  );
};

