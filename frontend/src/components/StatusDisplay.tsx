import { Status } from '../types';

interface StatusDisplayProps {
  status: Status;
  message?: string;
  jobTitle?: string;
  company?: string;
}

export const StatusDisplay = ({ status, message, jobTitle, company }: StatusDisplayProps) => {
  if (status === 'idle') return null;

  const statusColors = {
    pending: '#FFA500',
    success: '#28A745',
    failure: '#DC3545'
  };

  return (
    <div style={{
      marginTop: '20px',
      padding: '16px',
      borderRadius: '8px',
      backgroundColor: '#F8F9FA',
      border: `2px solid ${statusColors[status]}`,
      color: '#333'
    }}>
      <div style={{ fontWeight: 'bold', marginBottom: '8px', color: statusColors[status] }}>
        {status.toUpperCase()}
      </div>
      {message && <div>{message}</div>}
      {jobTitle && <div style={{ marginTop: '8px' }}>Job: {jobTitle}</div>}
      {company && <div>Company: {company}</div>}
    </div>
  );
};

