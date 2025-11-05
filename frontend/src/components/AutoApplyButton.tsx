import { useState } from 'react';
import { autoApply } from '../utils/api';
import { hardcodedPreferences } from '../utils/preferences';
import { StatusDisplay } from './StatusDisplay';
import { Status } from '../types';

export const AutoApplyButton = () => {
  const [status, setStatus] = useState<Status>('idle');
  const [message, setMessage] = useState<string>('');
  const [jobTitle, setJobTitle] = useState<string>('');
  const [company, setCompany] = useState<string>('');

  const handleApply = async () => {
    setStatus('pending');
    setMessage('Applying...');
    setJobTitle('');
    setCompany('');

    try {
      const result = await autoApply(hardcodedPreferences);
      setStatus(result.success ? 'success' : 'failure');
      setMessage(result.message);
      setJobTitle(result.jobTitle || '');
      setCompany(result.company || '');
    } catch (error) {
      setStatus('failure');
      setMessage(error instanceof Error ? error.message : 'Application failed');
    }
  };

  return (
    <div>
      <button
        onClick={handleApply}
        disabled={status === 'pending'}
        style={{
          padding: '12px 24px',
          fontSize: '16px',
          backgroundColor: status === 'pending' ? '#CCC' : '#007BFF',
          color: 'white',
          border: 'none',
          borderRadius: '8px',
          cursor: status === 'pending' ? 'not-allowed' : 'pointer',
          fontWeight: 'bold'
        }}
      >
        {status === 'pending' ? 'Applying...' : 'Auto Apply'}
      </button>
      <StatusDisplay status={status} message={message} jobTitle={jobTitle} company={company} />
    </div>
  );
};

